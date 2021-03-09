def perfect(num):
    sum=0
    fac=1
    while fac<num:
        if num%fac==0:
            sum=sum+fac
        fac=fac+1
    if num==sum:
        print("it is a perfect number")
    else:
        print("it not a perfect number")
num=int(input("enter a number="))
perfect(num)