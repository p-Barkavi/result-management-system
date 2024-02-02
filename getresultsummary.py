def getresultsummary():
    # Import user utils and libs
    import dbconnectionutil
    mycon=dbconnectionutil.getconnection()
    a=input('Enter s for student result summary,t for subject wise teacher result summary:')
    if a=='s':
        stu=input('Enter student_id:')
        cur=mycon.cursor()
        query_str="select student_id from student_t where student_id={stu_id}".format(stu_id=stu)
        cur.execute(query_str)    
        st=len(cur.fetchall())
        
        pd=input('Enter the password:')
        cur=mycon.cursor()
        query_str1="select u.pwd from user_t u,student_t st where st.user_id=u.user_id and u.pwd='{pawd}'".format(pawd=pd)
        cur.execute(query_str1)
        p=len(cur.fetchall())
        
        if st==1 and p==1:
            exam=input('Enter exam_id:')
            cur=mycon.cursor()
            query_str2="select exam_id from exam_t where exam_id={exam_id}".format(exam_id=exam)
            cur.execute(query_str2)    
            e=len(cur.fetchall())
            if e==1:
                cur=mycon.cursor()
                #query_str3='select concat(u.firstnm,'',u.lastnm),c.class,c.section,e.exam_nm from student_t st,user_t u,class_t c,exam_t e where st.user_id = u.user_id and st.student_id ={stu_id} and st.class_id=c.class_id and e.exam_id={exam_id}'.format(stu_id=stu,exam_id=exam)
                query_str3='select u.firstnm,c.class,c.section,e.exam_nm from student_t st,user_t u,class_t c,exam_t e where st.user_id = u.user_id and st.student_id ={stu_id} and st.class_id=c.class_id and e.exam_id={exam_id}'.format(stu_id=stu,exam_id=exam)
                cur.execute(query_str3)
                rs=cur.fetchall()
                for i in rs:
                    tuple1 = ('student name','class','section','exam name')
                    tuple2 = i
                    if len(tuple1)==len(tuple2):
                        res1 = dict(zip(tuple1,tuple2))
                        print (str(res1)),'\n'                        

                cur=mycon.cursor()
                query_str4='select s.sub_name,ex.mark_scored,ex.mark_base,ex.mark_perct,ex.grade from student_t st,user_t u,exam_t e,exam_result_t ex,subject_t s where st.user_id=u.user_id and st.student_id = {stu_id} and e.exam_id={exam_id} and st.student_id =ex.student_id and ex.exam_id=e.exam_id and ex.subject_id = s.subject_id'.format(stu_id=stu,exam_id=exam)
                #query_str4='select s.sub_name,ex.mark_scored,ex.mark_base,ex.mark_perct,ex.grade from student_t st,user_t u,exam_result_t ex,subject_t s,exam_t e,class_t c where st.user_id = u.user_id and st.student_id ={stu_id} and s.subject_id=ex.subject_id and ex.student_id = st.student_id and st.class_id = c.class_id'.format(stu_id=stu)
                cur.execute(query_str4)
                re=cur.fetchall()
                print('\n')
                for i in re:
                    tuple3 = ('subject name','marks scored','mark base','percentage','grade')
                    tuple4 = i
                    if len(tuple3)==len(tuple4):
                        res = dict(zip(tuple3,tuple4))
                        print (str(res)),'\n'

            else:
                print('Invaild Exam id')
        else:
            print('Invaild password and student id')
            
    elif a=='t':
        tea=input('Enter Teacher_id:')
        cur=mycon.cursor()
        query_str="select teacher_id from teacher_t where teacher_id={tea_id}".format(tea_id=tea)
        cur.execute(query_str)    
        t1=len(cur.fetchall())

        pwd=input('Enter password:')
        cur=mycon.cursor()
        query_str1="select pwd from user_t u,teacher_t t where t.user_id=u.user_id and u.pwd='{pawd}'".format(pawd=pwd)
        cur.execute(query_str1)    
        p=len(cur.fetchall())
        
        if t1==1 and p==1:
            cls=input('Enter class_id:')
            cur=mycon.cursor()
            query_str2="select class_id from class_t where class_id={c_id}".format(c_id=cls)
            cur.execute(query_str2)    
            c=len(cur.fetchall())
            
            if c==1:
                exm=input('Enter exam_id:')
                cur=mycon.cursor()
                query_str3="select exam_id from exam_t where exam_id={e_id}".format(e_id=exm)
                cur.execute(query_str3)    
                ex=len(cur.fetchall())
                print(ex)
                if ex==1:
                    cur=mycon.cursor()
                    query_str4='select u.firstnm,c.class,c.section,sb.sub_name,e.exam_nm from user_t u,teacher_t t,class_t c,cst_t cs,subject_t sb,exam_t e where t.teacher_id={tea_id} and t.user_id=u.user_id and c.class_id={c_id} and c.class_id=cs.class_id and t.teacher_id=cs.teacher_id and cs.subject_id=sb.subject_id and e.exam_id={e_id}'.format(tea_id =tea,c_id = cls,e_id = exm)
                    cur.execute(query_str4)
                    rs=cur.fetchall()
                    for i in rs:
                        tuple1 = ('Teacher name','class','section','Subject name','exam name')
                        tuple2 = i
                        if len(tuple1)==len(tuple2):
                            res1 = dict(zip(tuple1,tuple2))
                            print (str(res1)),'\n'
                            
                    cur=mycon.cursor()
                    query_str5='select u.firstnm,ex.mark_scored,ex.mark_base,ex.mark_perct,ex.grade from user_t u,teacher_t t,class_t c,cst_t cs,subject_t sb,exam_t e,exam_result_t ex,student_t st where t.teacher_id={tea_id} and st.user_id=u.user_id and c.class_id={c_id} and c.class_id=cs.class_id and t.teacher_id=cs.teacher_id and cs.subject_id=sb.subject_id and e.exam_id={e_id} and e.exam_id=ex.exam_id and sb.subject_id=ex.subject_id and st.student_id=ex.student_id'.format(tea_id =tea,c_id = cls,e_id = exm)
                    cur.execute(query_str5)
                    re=cur.fetchall()
                    print('\n')
                    for i in re:
                        tuple3 = ('Student name','marks scored','mark base','percentage','grade')
                        tuple4 = i
                        if len(tuple3)==len(tuple4):
                            res = dict(zip(tuple3,tuple4))
                            print (str(res)),'\n'

                else:
                    print('Invalid Exam ID')            
            else:
                print('Invalid Class ID')        
        else:
            print('Invalid Password or Teacher ID')
    else:
        print('Invaild input')
        


