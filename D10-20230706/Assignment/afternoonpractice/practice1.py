num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

def addition(num1,num2):
    if num1 and num2>=10:
        return num1+num2
    else:
        return num1-num2

print(addition(num1,num2))


