def calculator (operation):
    i=0
    e=[]
    f=[]
    g=[]
    h=[]
    while i<len(num1):
        if operation=="add":
            a=num1[i]+num2[i]
            e.append(a) 
        if operation=="subtract":
            b= num1[i]-num2[i]
            f.append(b)  
        if operation=="multiply":
            c=num1[i]*num2[i]
            g.append(c)
        if operation=="divide":
            d=num1[i]/num2[i]
            h.append(d)
        i=i+1
    return g
num1=[5,10,50,20]
num2=[2,20,3,5]
total=calculator("multiply")
print(total)