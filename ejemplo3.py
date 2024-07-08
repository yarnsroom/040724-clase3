"""
print("welcome to the basic calculator program UWU")
number1 = float(input("please enter the number 1:"))
number2 = float(input("please enter the number 2:"))
add=number1+number2
multiply=number1*number2
subtraction = number1-number2
division=number1/number2
print("the sum of the two number is:", add)
print("the subtraction of the two number is:", subtraction)
print("the multiplication of the two number is:", multiply)
print("the division of the two number is:", division)
print("")
print("program end!!!")
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