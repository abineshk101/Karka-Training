# list1=[]
# n=1
# while n<=10:
#     user=input("Enter the voting member 'A' or 'B' or 'C':")
#     user1=user.upper()
#     if user1=="A" or user1=="B" or user1=="C":
#         list1.append(f"candidate {user1}")
#         n=n+1
#     else:
#         print("Please vote first")

list1=[]
votelist={}
while len(list1)<10:
    user=input("Enter the voting member 'A' or 'B' or 'C':")
    user1=user.upper()
    if user1=="A" or user1=="B" or user1=="C":
        list1.append(f"candidate {user1}")
    else:
        print("Please vote first")
votelist["candidate A"]=list1.count("candidate A")
votelist["candidate B"]=list1.count("candidate B")
votelist["candidate C"]=list1.count("candidate C")
print(votelist)