def calculator (operation):
    if operation=="add":
        a=num1+num2
        return a
    if operation=="subtract":
        b= num1-num2
        return b
    if operation=="multiply":
        c=num1*num2
        return c
    if operation=="divide":
        d=num1/num2
        return d
num1=int(input("enter a number="))
num2=int(input("enter a number="))
add_result=calculator("add")
print(add_result)
subtract_result=calculator("subtract")
print(subtract_result)
multiply_result=calculator("multiply")
print(multiply_result)
divide_result=calculator("divide")
print(divide_result)
