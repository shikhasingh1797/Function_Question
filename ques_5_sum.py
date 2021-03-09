n=int(input("enter a number="))
i=0
while i<n:
    user=input("enter the number=")
    length=len(user)
    integer=int(user)
    f_len=length-1
    x="1"
    y="0"
    i=0
    c=" "
    c=c+x
    while i<f_len:
        c=c+y
        i=i+1
        m=int(c)
        a=integer%10
        b=integer//m
print(a+b)