num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
# number=0
# if num1>number:
#     number=num1
# if num2>number:
#     number=num2
# if num3>number:
#     number=num3
# print(f"The largest number is {number}")

if num1>num2:
    if num1>num3:
        print(f"The largest number is {num1}")
    else:
        print(f"The largest number is {num3}")
elif num2>num1:
    if num2>num3:
        print(f"The largest number is {num2}")
    else:
        print(f"The largest number is {num3}")
elif num3>num1:
    if num3>num2:
        print(f"The largest number is {num3}")
    else:
        print(f"The largest number is {num2}")