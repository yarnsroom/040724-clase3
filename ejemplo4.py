"""
print("welcome to the basic calculator program UWU")
number1 = float(input("please enter the number 1:"))
number2 = float(input("please enter the number 2:"))
option=int(input(print("please enter a opcion: 1)sum, 2)subtraction, 3)multiplication, 4)division")))
if option ==1:
    result=number1+number2
    oper="sum"
elif option ==2:
    result = number1-number2
    oper="subtraction"
elif option==3:
    result=number1*number2
    oper="multiplication"
elif option==4:
    result=number1/number2
    oper="division"
else:
    result=0
    oper=("error! invalid operation!")
print("the operation is:", oper, "and the result is:", result)
print("")
print("program end!!!")
"""

answer="y"
oper=""
number1=0
number2=0
result=0
def operation(num1, num2, opt):
    global result
    global oper
    if option ==1:
        result=number1+number2
        oper="sum"
    elif option ==2:
        result = number1-number2
        oper="subtraction"
    elif option==3:
        result=number1*number2
        oper="multiplication"
    elif option==4:
        result=number1/number2
        oper="division"
    else:
        result=0
        oper="error! invalid operation!"

print("welcome to the basic calculator program UWU")


while answer == "y":
    number1 = float(input("please enter the number 1: "))
    number2 = float(input("please enter the number 2: "))
    option=int(input(print("please enter a opcion: 1)sum, 2)subtraction, 3)multiplication, 4)division")))
    operation(number1, number2, option)
    print("the operation is:", oper, "and the result is:", result)
    answer = input("would you like to continue? yes(y), no(n)")
print("")
print("program end!!!")