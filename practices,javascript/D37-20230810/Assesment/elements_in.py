s="abcabcbbcaks" 
ans=""
for item in s:
    if item not in ans:
        ans+=item
print(ans)
