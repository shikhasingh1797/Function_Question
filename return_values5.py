def calculator (num1,num2,operation):
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
print(calculator(50,75,"subtract"))
