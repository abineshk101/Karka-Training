list1=[3,2,2,3]
num=2
list2=[]
for i in range(len(list1)):
    if list1[i]!=num:
        list2.append(list1[i])
for n in range(len(list1)):
    if list1[n]==num:
        list2.append("*")
print(list2)

# value=list1.count(num)
# for n in range(value):
#     list2.append("*")
# print(list2)