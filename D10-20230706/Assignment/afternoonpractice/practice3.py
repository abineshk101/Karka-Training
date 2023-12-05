list1=[69,81,89,55,72]
value=0

for num in list1:
    value=value+num

avg=value/len(list1)

if avg>80:
    print("eligible")
else:
    print("not eligible")

