#import the functions
import createexam, createclass, createstudent, createteacher, uploadresult,assignteachers,getresultsummary
print("WELCOME TO RESULT MANAGEMENT SYSTEM")
print("====================================================")
print("Check out the following things we can do for you!")
print("1.create a user with teacher authorization")
print("2.create a user with student authorization")
print("3.create a class")
print("4.create an exam")
print("5.upload result for a batch,subject-wise")
print("6.assign the subject teachers to a class")
print("7.get the result for a student or a class")
print("====================================================")
func=int(input("enter the number of the function you would like to do:"))
if func==1:
    createteacher.createteacher()
elif func==2:
    createstudent.createstudent()
elif func==3:
    createclass.createclass()
elif func==4:
    createexam.createexam()
elif func==5:
    uploadresult.uploadresult()
elif func==6:
    assignteachers.assignteachers()
elif func==7:
    getresultsummary.getresultsummary()
else:
    print("This system is not programmed to do this  function we apologise for the discomfort")
    
