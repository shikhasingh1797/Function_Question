num=[1,3,8,67,12,50,49]
def list1(num):
    i=0
    x=0
    while i<len(num):
        if x<num[i]:
            x=num[i]
        i=i+1
    print(x)
list1(num)