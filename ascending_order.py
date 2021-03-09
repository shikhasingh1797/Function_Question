a=[11,9,24,12,5]
def list1(a):
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[i]<a[j]:
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
            j=j+1
        i=i+1
    print(a)
list1(a)