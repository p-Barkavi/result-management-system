def createteacher():
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
                inputfile = input("enter the inputfile name including the extension containing teacher info:")
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

                    #Create insert sql for user_t table part
                    userinsertsql1 = 'insert into user_t('
                    userinsertsql2 = 'values('
                    userinsertsql = ''
                    firstvalue = True
                    uidposition=0
                    iterator=0
                    for field in fields:
                        if(firstvalue):
                            firstvalue = False
                            userinsertsql1 = userinsertsql1 + field
                            userinsertsql2 = userinsertsql2 + '%s'
                        else:
                            userinsertsql1 = userinsertsql1 + ', ' + field
                            userinsertsql2 = userinsertsql2 + ', %s'
                        if field.lower=='user_id':
                            uidposition=iterator
                        iterator+=1
                    

                    userinsertsql = userinsertsql1 + ', active, crt_dttm, updt_dttm) ' + userinsertsql2 + ', %s, %s, %s)'
                    print('Insert Sql: '+ userinsertsql)

                    teacherinsertsql='insert into teacher_t (teacher_id,user_id,crt_dttm,upd_dttm) \
                                    values (%s,%s,%s,%s)'
                    
                    # Process the data rows
                    formatted_date = datetimeutil.getcurrenttime()
                    print("Time now: " + formatted_date)
                    cursor = cnx.cursor()
                    for row in rows:
                        ## Append active status,current time for create date time and update date time
                        row.append('y')
                        row.append(formatted_date)
                        row.append(formatted_date)
                        cursor.execute(userinsertsql,tuple(row))
                        #creating student
                        user_id=row[uidposition]
                        teacherval=(user_id,user_id,formatted_date,formatted_date)
                        cursor.execute(teacherinsertsql,teacherval)

                    ## Commit Transction
                    cnx.commit()
                except IOError:
                    print ("Could not read file:" + inputfile)
                print ("The data read from CSV has been appended to SQL")                    
            else:
                print("You do not have privileges to create an teacher")
    dbconnectionutil.closeconnection(cnx)
