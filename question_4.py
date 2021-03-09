# def add_numbers(numbaer1,number2):
#     print(number1+number2)
# number1=int(input("enter a num="))
# number2=int(input("enter a num="))
# add_numbers(number1,number2)



def add(num):
    i=0
    sum=0
    a=[]
    while i<len(num):
        sum=2+num[i]
        a.append(sum)
        i=i+1
    print(a)
num=[4,6,8,10,12]
add(num)