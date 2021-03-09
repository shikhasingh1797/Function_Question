print('Kaun bnega crorepati me aapka swagat hai , ab first question ye rha aapki screen par....')
lis=['how many continents are there?','what is the capital of india','ng me kaun sa course padhaya jata hai']
opt=[['four','nine','seven','eight'],['chandigadh','bhopal','chennai','delhi'],['software engineering','counsling','tourism','agriculture']]
solution=[3,4,1]
option1=[['seven ','eight'],['chennai','delhi'],['software engineering','counsling']]
solution1=[1,2,1]
count=0
def lifeline(index):
    global count
    i=0
    if count==0:
        while i<len(option1[index]):
            print(i+1,option1[index][i])
            i=i+1
        user_ans=int(input("enter the num"))
        count+=1
        if user_ans==solution1[index]:
            return True
        else:
            return False
    else:
        print("you use 5050")
        return "no"
def option(index):
    j=0
    while j<len(opt[index]):
        print(j+1,opt[index][j])
        j+=1
    user_ans=int(input("enter the option"))
    if user_ans==solution[index]:
        return True
    if user_ans==5050:
        return(lifeline(index))

    else:
        return False

def que():
    index=0
    while index<len(lis):
        print(index+1,lis[index])
        result=option(index)
        if result=="no":
            index-=1
        elif result==True:
            print("congrates")
        else:
            print("you loos")
            break
        index+=1
def main():
    que()
main()