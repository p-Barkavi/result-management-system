def enterresult():
    # Import user utils and libs
    import dbconnectionutil, validateuserutil, datetimeutil
    import csv
    #Check user credentials
    cnx=dbconnectionutil.getconnection()
    user=int(input('enter your Admin id:'))
    if(validateuserutil.checkuser(cnx,user)):
        print("vaild user")
        pwd=input("enter your password here:")
        if(validateuserutil.checkpassword(cnx,user,pwd)):
            print("vaild password")
            if(validateuserutil.checkrole(cnx,user,'teacher')):
                ex_id=int(input("enter the exam id for which the batch of results is to be uploaded:")) 
                sub_id=int(input("enter the subject id for which batch of results is to be uploaded:"))
                inputfile = input("enter the inputfile name including the extension which contains the results:")
                # initializing the fields and rows list
                fields = []
                rows = []
                
                # Load csv file
                try:
                    # Reading csv file
                    with open(inputfile, 'r') as csvfile:
                        #Create csv reader
                        csvreader = csv.reader(csvfile)

                        # extracting field names through first row
                        fields = next(csvreader)
                        
                        # extracting each data row one by one
                        for row in csvreader:
                            rows.append(row)

                    # Total number of rows
                    print("Total no. of rows: %d"%(csvreader.line_num))
                      
                    # Field names in the file header
                    # print('Field names are: ' + ', '.join(field for field in fields))

                    #Create insert sql for exam_t table part
                    examinsertsql1 = 'insert into exam_t('
                    examinsertsql2 = 'values('
                    examinsertsql = ''
                    firstvalue = True
                    for field in fields:
                        if(firstvalue):
                            firstvalue = False
                            examinsertsql1 = examinsertsql1 + field
                            examinsertsql2 = examinsertsql2 + '%s'
                        else:
                            examinsertsql1 = examinsertsql1 + ', ' + field
                            examinsertsql2 = examinsertsql2 + ', %s'

                    examinsertsql = examinsertsql1 + ',subject_id,exam_id, crt_dttm, upd_dttm) ' + examinsertsql2 + ', %s, %s, %s, %s)'
                    print('Insert Sql: '+ examinsertsql)

                    # Process the data rows
                    formatted_date = datetimeutil.getcurrenttime()
                    print("Time now: " + formatted_date)
                    cursor = cnx.cursor()
                    for row in rows:
                        ## Append subjectid, examid and current time for create date time and update date time
                        row.append(sub_id)
                        row.append(ex_id)
                        row.append(formatted_date)
                        row.append(formatted_date)
                        cursor.execute(examinsertsql,tuple(row))
                        
                    ## Commit Transction
                    cnx.commit()
                except IOError:
                    print ("Could not read file:" + inputfile)
                print ("The data read from CSV has been appended to SQL")                    
            else:
                print("You do not have privileges to enter the result")
    dbconnectionutil.closeconnection(cnx)
