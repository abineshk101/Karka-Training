nums=[[1,2],[3,4]]
input1=input("Enter the operation ").lower()
a=0
b=[]
c={}
ans=None
for i in range(len(nums)):
    for n in nums[i]:
        if input1=="add":
            a+=n
        elif input1=="sub":
            a-=n
            ans=a
        elif input1=="list":
            b.append(n)
            ans=(b)
        elif input1=="dictionary":
            b.append(n)
            c[f"index{n-1}"]=n
            ans=c
        elif input1=="string":
            b.append(n)
            ans=f"'{str(b)}'"
        elif input1=="tuple":
            b.append(n)
            ans=tuple(b)
        elif input1=="set":
            c.add(str(n))
            ans=c

print(ans)

        