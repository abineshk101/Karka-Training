list1=[1,2,4,1,4]
list2=[3,1,7]
ans=[]
len1=len(list1)
len2=len(list2)

if len1!=len2:
    count=abs(len1-len2)
for i in range(count):
    if len1>len2:
        list2.append(0)
    else:
        list1.append(0)
for n in range(len1):
    if list1[n]>list2[n]:
        ans.append(list1[n])
    else:
        ans.append(list2[n])
print(ans)