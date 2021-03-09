def eligible_for_vote(age):
    if age<=18:
        print("not eligible")
    else:
        print("you are eligible")
age=int(input("enter your age="))
eligible_for_vote(age)