input1=["flower","flw","foight"]
length=len(input1[0])
item=input1[0]
for n in input1:
    ans=""
    if len(n)<length:
        item=n
    for l in n:
        if l in item:
            ans=ans+l
        else:
            break
print(ans)

        
    