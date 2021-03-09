a=[1,2,3,4,5,6,7,8,9,10,11]
def list1():
    c=[]
    b=[]
    cou1=0
    cou2=0
    i=0
    while i<len(a):
        if a[i]%2==0:
            cou1=cou1+1
            c.append(a[i])
        else:
            cou2=cou2+1
            b.append(a[i])
        i=i+1
    print("total even number=",cou1,a)
    print("total odd number=",cou2,b)
list1()
