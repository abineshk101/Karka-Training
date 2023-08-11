a=[1,2,0,3,5,0,9,0,7]
ans=[]
for n in a:
    ans+=[n]
    if n==0:
        ans+=[0]
    if len(a)==len(ans):
        break
print(ans)