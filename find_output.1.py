# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak") 





#niche diye gye code snippet ki output kya hogi?

def primeorNot(num):     
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")

    else:
           print(num,"is not a prime number")
primeorNot(406)