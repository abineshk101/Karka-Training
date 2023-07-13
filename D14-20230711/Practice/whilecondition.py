print("I will add up the numbers you give me. ")
total=0
value=1
while value!=0:
    value=int(input("Enter the number "))
    total=total+value
    print(f"The number is so far {total}")
    if value==0:
        print(f"The total is {total}")

