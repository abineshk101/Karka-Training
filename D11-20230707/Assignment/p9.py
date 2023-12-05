# def dayfind(n):
#     if n==0:
#         return "Sunday"
#     elif n==1:
#         return "Monday"
#     elif n==2:
#         return "Tuesday"
#     elif n==3:
#         return "Wednesday"
#     elif n==4:
#         return "Thursday"
#     elif n==5:
#         return "Friday"
#     elif n==6:
#         return "Saturday"
#     else:
#         return "Not defined"
# day=int(input("Enter the number"))
# print(dayfind(day))

week=["sunday","Monday","Tuesday","wednesday","Thursday","Friday","Saturday"]
num=int(input("Enter the weekday "))-1
if num>7:
    print("not defined")
else:
    print(f"Today is a {week[num]}")