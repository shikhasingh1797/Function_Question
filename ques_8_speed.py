def check(speed):
    if speed<70:
        print("ok")
    elif speed>=130:
        print("license suspended")
    elif speed>70:
        a=speed-70
        b=a//5
        print("points:",b)
num=int(input("enter a number="))
check(num)