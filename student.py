days=int(input("number of total days:"))
n=int(input("enter the number of students:"))
student_list=[]
for i in range(0,n):
 name=input("name of the student:")
 attendance=int(input("attendance of the students:"))
 percentage=((attendance/days)*100)
 student_list.append((name,percentage))
 student_list.sort()
print(student_list)
for i in student_list:
 	print(i[0],i[1]) 
