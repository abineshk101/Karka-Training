def arithin(a,operator,b):
    if operator=="+":
        return a+b
    elif operator=="-":
        return a-b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b

def greetings():
    return "hai, Thank You"


def checkUserOption():
    user=input("If you want to continue press say 'yes' or 'no' ")
    if user=="yes":
        n1=int(input("Enter the first number"))
        operator=input("Enter the operator")
        n2=int(input("Enter the second number"))
        print(arithin(n1,operator,n2))
        checkUserOption()
    else:
        print(greetings())

checkUserOption()


