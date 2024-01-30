num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
operation=input("choose an arithematic operations(+,-,*,/,** for exponetion,// for floor divisionand% for modulo):")
if operation=="+":
   result=num1+num2
elif operation=="-":
     result=num1-num2
elif operation=="*":
     result=num1*num2
elif operation=="/":
     result=num1/num2
elif operation=="**":
     result=num1**num2
elif operation=="//":
     result=num1//num2
elif operation=="%":
     result=num1%num2
else:
     print("invalid input")
print("the result of the arithematic operation is:",result)
     
