l=[1,0,3,0,9,13]
for i in range(len(l)):
    for n in range(i+1,len(l)):
        if l[i]==l[n]:
            a=l[i]
            l.remove(a)
            num=l.count(a)
            for j in range(num):
                l.append(a)
print(l)