input1="Hi I am Abinesh from Vattavilai"
list1=input1.split(" ")
longest=list1[0]
for item in list1:
    if len(item)>len(longest):
        longest=item
print(longest)