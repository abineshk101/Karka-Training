list1=[9]
ans=[]
value=""
for n in list1:
    value+=str(n)
value=int(value)+1
for i in str(value):
    ans.append(int(i))
print(ans)


