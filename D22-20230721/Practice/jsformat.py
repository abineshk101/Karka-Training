import json
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
    dictionary["month"]=i+1
    dictionary["unit"]=unit
    dictionary["amount"]=amount
    bill_list.append(dictionary)
data=bill_list

data1=str(data)
input1=input("Enter the type which you want to save the file in json form or in dictionary form or in string form: ")
input1=input1.lower()
if input1=="json":
      convert=json.dumps(data1)
      file=open("/home/abinesh/Documents/jsformat","w")
      file.write(convert)
      file.close()
elif input1=="dictionary":
      file=open("/home/abinesh/Documents/jsformat","w")
      file.write(data1)
      file.close()
elif input1=="string":
      file=open("/home/abinesh/Documents/jsformat","w")
      for dictionaries in data:
            for key,value in dictionaries.items():
                  file.write(f"{str(key)}:{str(value)}\n")
            file.write("\n")
file.close()
