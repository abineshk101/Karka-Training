yr=input("Enter the year ")
yr=int(yr)
cond1=yr%4
cond2=yr%100
cond3=yr%400
if cond1==0 and cond2!=0 or cond3==0:
    print(yr," is a leap year")
else:
    print(yr," is not a leap year")


# yr=input("Enter the year ")
# yr=int(yr)
# if yr%4==0 and yr%100!=0 or yr%400==0:
    # print(yr," is a leap year")
# else:
    # print(yr," is not a leap year")
