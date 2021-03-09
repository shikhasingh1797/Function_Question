print("Welcome")
print("Insert your card")
language=input("enter your language hindi= or english=")
if language=="hindi":
    print("aapne hindi language select kiya hai")
if language=="english":
    print("you selected english language")
i=0
trans=["withdraw","deposit","check your balance","quit"]
option=[1,2,3,4]
while i<len(trans):
    print(i+1,trans[i])
    i=i+1
total_amount=10000
trans=int(input("select any option="))
if trans==1:
    password=int(input("enter your password="))
    if password==1384:
        cash=int(input("enter your cash="))
        a=total_amount-cash
        print("aapne",cash,"rupees withdraw kiye hai ab aapke account me",a,"rupees shesh bache hai")
    if password!=1384:
        print("your password is wrong please put correct password")
if trans==2:
    deposit=int(input("how much you want to deposit="))
    pin=int(input("enter your pin="))
    if pin==1384:
        b=total_amount+deposit
        print("aapne",deposit,"rupees deposit kiye hai ab aapke account me total balance",b,"hai")
    if pin!=1384:
        print("wrong password put right password")
if trans==3:
    password=int(input("enter your pass="))
    if password==1384:
        print("total balance in your account=",total_amount)
    if password!=1384:
        print("wrong password")
if trans==4:
    print("quit")
