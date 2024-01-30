def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def pow(num1,num2):
    return num1**num2
def calculator(num1,operator,num2):
 if operator=="+":
   return add(num1,num2)    
 elif operator=="-":
   return sub(num1,num2) 
 elif operator=="*":
   return mul(num1,num2)
 elif operator=="/":
   return div(num1,num2) 
 elif operator=="**":
   return pow(num1,num2)    
 else:   
      print("invalid input")
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
operator=input("choose an arithmetic operator(+,-,*,/,**):")
result=calculator(num1,operator,num2)
print(result)

