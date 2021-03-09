def multiple(limit):
    i=1
    sum=0
    while i<=num:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    return sum
num=int(input("enter a number="))
print(multiple(num))