def perfect():
    i=1
    while i<10000:
        fac=1
        sum=0
        while fac<i:
            if i%fac==0:
                sum=sum+fac
            fac=fac+1
        if sum==i:
            print(i,"it is a perfect number")
        i=i+1
perfect()