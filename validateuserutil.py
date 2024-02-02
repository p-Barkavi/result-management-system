def checkuser(cnx,user):
    rvalue = False
    cursor=cnx.cursor()
    sql='select * from user_t where user_id= %s'
    cursor.execute(sql % user)
    result=cursor.fetchall()
    rc=cursor.rowcount
    if rc!=1:
        print("Invalid user id")
    elif rc==1:
        rvalue=True
    return rvalue;

def checkpassword(cnx,user,pwd):
    rvalue = False
    cursor=cnx.cursor()
    sql='select * from user_t where user_id=%s and pwd=%s'
    cursor.execute(sql,(user,pwd))
    result=cursor.fetchall()
    rc=cursor.rowcount
    if rc!=1:
        print("Invalid password")
    elif rc==1:
        rvalue=True
    return rvalue;

def checkrole(cnx,user,role):
    rvalue = False
    if(role.lower()=='admin'):
        cursor=cnx.cursor()
        sql='select * from admin_t where user_id=%s'
        cursor.execute(sql % user)
        result=cursor.fetchall()
        rc=cursor.rowcount
        if rc!=1:
            print("Not an administrator")
        elif rc==1:
            rvalue=True
    elif(role.lower()=='teacher'):
        cursor=cnx.cursor()
        sql='select * from teacher_t where user_id=%s'
        cursor.execute(sql % user)
        result=cursor.fetchall()
        rc=cursor.rowcount
        if rc!=1:
            print("Not an teacher")
        elif rc==1:
            rvalue=True  
    elif(role.lower()=='student'):
        cursor=cnx.cursor()
        sql='select * from student_t where user_id=%s'
        cursor.execute(sql % user)
        result=cursor.fetchall()
        rc=cursor.rowcount
        if rc!=1:
            print("Not an student")
        elif rc==1:
            rvalue=True  
    else:
        print("Unknown role")
    return rvalue;
    
        

