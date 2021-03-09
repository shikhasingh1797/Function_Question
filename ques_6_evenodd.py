def showNumbers(limit):
    i=0
    while i<=num:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i=i+1
num=int(input("enter a number="))
showNumbers(num)