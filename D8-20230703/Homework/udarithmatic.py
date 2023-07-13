def arithin(n1,operator,n2):
    if operator=="+":
        return n1+n2
    elif operator=="-":
        return n1-n2
    elif operator=="*":
        return n1*n2
    elif operator=="**":
        return n1**n2
    elif operator=="/":
        return n1/n2
    elif operator=="%":
        return n1%n2
    else:
        return "not defined"

n1=int(input("Enter the first number "))
operator=input("Enter the operator")
n2=int(input("Enter the second number "))
result=arithin(n1,operator,n2)
print(result)
