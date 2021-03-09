# def check_numbers(num,num1):
#     if num %2==0 and num1%2==0:
#         print("both numbers are even")
#     else:
#         print("both numbers are not even")
# num=int(input("enter any number="))
# num1=int(input("enter any number"))
# check_numbers(num,num1)



def check_numbers(num,num1):
    i=0
    while i<len(num):
        if num[i]%2==0 and num1[i]%2==0:
            print("both even number")
        else:
            print("both are not even numbers")
        i=i+1
num=[2,6,18,10,3,75]
num1=[6,19,24,12,3,87]
check_numbers(num,num1)