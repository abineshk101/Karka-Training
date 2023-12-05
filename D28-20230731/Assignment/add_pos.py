l=[1,5,3,7,9,13]
list1=[]
for i in range(len(l)):
    for n in range(len(l)):
        if l[n]==l[i]:
            continue
        ans=(l[i]+l[n])
        if ans==10:
            list1.append(i)
            list1.append(n)
        break
print(list1)