def uploadresult():
    # Import user utils and libs
    import dbconnectionutil, validateuserutil, datetimeutil
    import csv
    #Check user credentials
    cnx=dbconnectionutil.getconnection()
    user=int(input('enter your Teacher id:'))
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

                    #Create insert sql for exam_result_t table part
                    resultinsertsql1 = 'insert into exam_result_t('
                    resultinsertsql2 = 'values('
                    resultinsertsql = ''
                    firstvalue = True
                    for field in fields:
                        if(firstvalue):
                            firstvalue = False
                            resultinsertsql1 = resultinsertsql1 + field
                            resultinsertsql2 = resultinsertsql2 + '%s'
                        else:
                            resultinsertsql1 = resultinsertsql1 + ', ' + field
                            resultinsertsql2 = resultinsertsql2 + ', %s'

                    resultinsertsql = resultinsertsql1 + ',subject_id,exam_id, crt_dttm, upd_dttm) ' + resultinsertsql2 + ', %s, %s, %s, %s)'
                    print('Insert Sql: '+ resultinsertsql)

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
                        cursor.execute(resultinsertsql,tuple(row))
                        
                    ## Commit Transction
                    cnx.commit()
                except IOError:
                    print ("Could not read file:" + inputfile)
                print ("The data read from CSV has been appended to SQL")
            else:
                print("You do not have privileges to create an Exam Result")
    dbconnectionutil.closeconnection(cnx)
