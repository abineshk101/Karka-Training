data={"name":"Abinesh",
      "readings":[1100,1200,1350,1650,2050]}
print(f"Consumer name:",data["name"])
bill_list=[]
total=0
for i in range(len(data["readings"])-1):
    dictionary={}
    unit=data["readings"][i+1]-data["readings"][i]
    if unit<100:
        amount=0
    elif 100<=unit<200:
        amount=unit*2
    elif 200<=unit<500:
        amount=unit*5
    elif 500<=unit<1000:
        amount=unit*10
    elif unit>=1000:
        amount=unit*14
    total=total+amount
#     print("\nmonth",i+1)
#     print(f"unit consumed is:{unit}")
#     print(f"amount for this month {amount}")
# print(f"\nThe total amount is {total}")

    dictionary["month"]=i+1
    dictionary["unit"]=unit
    dictionary["amount"]=amount
    bill_list.append(dictionary)
print(bill_list)
    

    