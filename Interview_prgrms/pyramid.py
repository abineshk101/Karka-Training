l=5
for n in range(l):
    print(" "*(l-n-1),end="")
    for i in range(n+1):
        print(" *",end="")
    print(" ")