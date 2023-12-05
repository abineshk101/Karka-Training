l=[1,0,3,0,9,13]
for n in l:
    if n==0:
        l.remove(n)
        l.append(0)
print(l)