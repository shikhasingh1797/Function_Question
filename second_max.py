num=[10,15,20,12,28]
def list1(num):
    z=len(num)
    max1=num[0]
    max2=num[1]
    i=0
    while i<z:
        if num[i]>max1:
            max2=max1
            max1=num[i]
        elif max1>num[i]>max2:
            max2=num[i]
        i=i+1
    print("maximum number=",max1)
    print("second maximum number",max2)
list1(num)