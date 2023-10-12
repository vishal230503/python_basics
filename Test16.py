courseList=["Python" , "Java" , "Oracle" , "C++" , "Mysql"]
print(courseList)
cname=input("Enter Course Name ")
if cname in courseList:
    print("Course Available")
else:
    print("Course Not Available");
