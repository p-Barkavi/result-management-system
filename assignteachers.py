def assignteachers():
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
            if(validateuserutil.checkrole(cnx,user,'admin')):
                cls_id=int(input("enter the class for which teachers should be assigned:"))
                inputfile = input("enter the inputfile name including the extension:")
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
                    cstinsertsql1 = 'insert into cst_t('
                    cstinsertsql2 = 'values('
                    cstinsertsql = ''
                    firstvalue = True
                    for field in fields:
                        if(firstvalue):
                            firstvalue = False
                            cstinsertsql1 = cstinsertsql1 + field
                            cstinsertsql2 = cstinsertsql2 + '%s'
                        else:
                            cstinsertsql1 = cstinsertsql1 + ', ' + field
                            cstinsertsql2 = cstinsertsql2 + ', %s'

                    cstinsertsql = cstinsertsql1 + ', class_id, crt_dttm, upd_dttm) ' + cstinsertsql2 + ', %s, %s, %s)'
                    print('Insert Sql: '+ cstinsertsql)

                    # Process the data rows
                    formatted_date = datetimeutil.getcurrenttime()
                    print("Time now: " + formatted_date)
                    cursor = cnx.cursor()
                    for row in rows:
                        ## Append current time for create date time and update date time
                        row.append(cls_id)
                        row.append(formatted_date)
                        row.append(formatted_date)
                        cursor.execute(cstinsertsql,tuple(row))
                        
                    ## Commit Transction
                    cnx.commit()
                except IOError:
                    print ("Could not read file:" + inputfile)
                print ("The data read from CSV has been appended to SQL")
            else:
                print("You do not have privileges to assign the teachers")
    dbconnectionutil.closeconnection(cnx)
