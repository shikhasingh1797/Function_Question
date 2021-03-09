def num(num):
    sum=0
    count=0
    temp=num
    while temp>0:
        count=count+1
        temp=temp//10
    temp=num
    while temp>0:
        rem=temp%10
        sum=sum+(rem**count)
        temp=temp//10
    if num==sum:
        print("it is a armstrong number")
    else:
        print("it is not a armstrong number")
num=int(input("enter any number="))
num(num)
