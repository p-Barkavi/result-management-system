Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py
WELCOME TO RESULT PROCESSING SYSTEM
====================================================
Check out the following things we can do for you!
1.create a user with teacher authorization
2.create a user with student authorization
3.create a class
4.create an exam
5.upload result for a batch,subject-wise
====================================================
enter the number of the function you would like to do:1
Connection to database successful
enter your user id:1
vaild user
enter your password here:admin@01
vaild password
enter the inputfile name including the extension containing teacher info:teacherinput.csv
Total no. of rows: 3
Insert Sql: insert into user_t(user_id, firstnm, lastnm, pwd, dob, gender, active, crt_dttm, updt_dttm) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
Time now: 2022-01-26 20:39:47
Time now: 2022-01-26 20:39:47
Traceback (most recent call last):
  File "C:\Program Files\Python39\lib\site-packages\mysql\connector\connection_cext.py", line 513, in cmd_query
    self._cmysql.query(query,
_mysql_connector.MySQLInterfaceError: Duplicate entry '6' for key 'user_t.PRIMARY'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py", line 14, in <module>
    createteacher.createteacher()
  File "C:\Users\kavin\OneDrive\Desktop\12CS\source code\createteacher.py", line 73, in createteacher
    cursor.execute(userinsertsql,tuple(row))
  File "C:\Program Files\Python39\lib\site-packages\mysql\connector\cursor_cext.py", line 269, in execute
    result = self._cnx.cmd_query(stmt, raw=self._raw,
  File "C:\Program Files\Python39\lib\site-packages\mysql\connector\connection_cext.py", line 518, in cmd_query
    raise errors.get_mysql_exception(exc.errno, msg=exc.msg,
mysql.connector.errors.IntegrityError: 1062 (23000): Duplicate entry '6' for key 'user_t.PRIMARY'
>>> 
= RESTART: C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py
WELCOME TO RESULT PROCESSING SYSTEM
====================================================
Check out the following things we can do for you!
1.create a user with teacher authorization
2.create a user with student authorization
3.create a class
4.create an exam
5.upload result for a batch,subject-wise
====================================================
enter the number of the function you would like to do:1
Connection to database successful
enter your user id:1
vaild user
enter your password here:admin@01
vaild password
enter the inputfile name including the extension containing teacher info:teacherinput.csv
Total no. of rows: 3
Insert Sql: insert into user_t(user_id, firstnm, lastnm, pwd, dob, gender, active, crt_dttm, updt_dttm) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
Time now: 2022-01-26 20:40:35
Time now: 2022-01-26 20:40:35
>>> 
=================================== RESTART: C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py ==================================
WELCOME TO RESULT PROCESSING SYSTEM
====================================================
Check out the following things we can do for you!
1.create a user with teacher authorization
2.create a user with student authorization
3.create a class
4.create an exam
5.upload result for a batch,subject-wise
====================================================
enter the number of the function you would like to do:2
Connection to database successful
enter your user id:2
vaild user
enter your password here:st@3
Invalid password
>>> 
=================================== RESTART: C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py ==================================
WELCOME TO RESULT PROCESSING SYSTEM
====================================================
Check out the following things we can do for you!
1.create a user with teacher authorization
2.create a user with student authorization
3.create a class
4.create an exam
5.upload result for a batch,subject-wise
====================================================
enter the number of the function you would like to do:2
Connection to database successful
enter your user id:2
vaild user
enter your password here:st@123
vaild password
Not an administrator
You do not have privileges to create an exam
>>> 
=================================== RESTART: C:\Users\kavin\OneDrive\Desktop\12CS\source code\RESULT_PROCESSING_SYSTEM.py ==================================
WELCOME TO RESULT PROCESSING SYSTEM
====================================================
Check out the following things we can do for you!
1.create a user with teacher authorization
2.create a user with student authorization
3.create a class
4.create an exam
5.upload result for a batch,subject-wise
====================================================
enter the number of the function you would like to do:3
Connection to database successful
enter your user id:2
vaild user
enter your password here:st@123
vaild password
Not an administrator
You do not have privileges to create an class
>>> 