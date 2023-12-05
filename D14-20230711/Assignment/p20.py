print("I will add up the numbers you give me. ")
total=0
for n in range(100):
    num=int(input("Number "))
    if num!=0:
        total=total+num
        print(f"The total is so far {total}")
    else:
        break
print(f"The total is {total}")

