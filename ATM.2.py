trans=["withdraw","deposit","check your balance","quit"]
print("Welcome")
print("Insert your card")
total_amount=10000
def language(lan):
    if lan=="hindi":
        print("aapne hindi language select kiya hai")
    if lan=="english":
        print("you selected english language")
def transjuction():
    i=0
    while i<len(trans):
        print(i+1,trans[i])
        i=i+1
def option(trans1):
    if trans1==1:
        withdraw()
    elif trans1==2:
        deposit()
    elif trans1==3:
        check_balance()
    else:
        quit()
def withdraw():
    password=int(input("enter your password="))
    if password==1384:
        cash=int(input("enter your cash="))
        a=total_amount-cash
        print("aapne",cash,"rupees withdraw kiye hai ab aapke account me",a,"rupees shesh bache hai")
    else:
        print("your password is wrong please put correct password")
def deposit():
    amount=int(input("enter your amount="))
    password=int(input("enter your password="))
    if password==1384:
        b=total_amount+amount
        print("aapne",amount,"rupees deposit kiye hai ab aapke account me total balance",b,"hai")
    elif password!=1384:
        print("wrong password put right password")
def check_balance():
    password=int(input("enter your password="))
    if password==1384:
        print("total balance in your account=",total_amount,"hai")
    elif password!=1384:
        print("wrong password")
def quit():
    print("quit")
lan=input("enter your language=")
language(lan)
transjuction()
trans1=int(input("enter any option="))
option(trans1)