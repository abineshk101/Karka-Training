data={"name":"Abinesh",
      "readings":[1100,1200,1350,1650,2050]}

def rate(a):
    if 100<=a<200:
        return a*2
    if 200<=a<500:
        return a*5
    if 500<=a<=1000:
        return a*10
    if a>1000:
        return a*14
    if a<100:
        return 0

amount_list=[]
unit=[]
reading1=data["readings"][0]
for reading in data["readings"][1:6]:
    value=reading-reading1
    reading1=reading
    amount_list.append(rate(value))
    unit.append(value)

total=0
for rupee in amount_list:
    total=total+rupee

# print(f"Consumer name:",(data["name"]))
# for i in range(len(unit)):
#     print("month:",i+1,f"\nReading:{unit[i]}\nAmount:{amount_list[i]}\n")
# print(f"The total amount is {total}")


print(f"Consumer name:",(data["name"]))
list1=[]
for i in range(len(unit)):
    all=({"month":i+1,"Reading":(unit[i]),"Amount":(amount_list[i])})
    list1.append(all)
print(list1)
print(f"\nThe total amount is {total}")
        
