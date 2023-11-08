list1=[3,2,2,3]
num=2
var=list1.count(num)
list1.remove(num)
for i in range(var):
    list1.append("*")
print(list1)