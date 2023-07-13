mark1=int(input("Enter the mark1 "))
mark2=int(input("Enter the mark2 "))
mark3=int(input("Enter the mark3 "))
mark4=int(input("Enter the mark4 "))
mark5=int(input("Enter the mark5 "))
total=mark1+mark2+mark3+mark4+mark5
print("The total mark is",total)
avg=total/5
print("Your average is",avg)
if avg>80:
    print("you got golden medal")
else:
    print("You got silver medal")