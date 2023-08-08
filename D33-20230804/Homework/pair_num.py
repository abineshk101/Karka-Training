nums = [2, 3, 5, 4, 7, 9, 8, 5]
ans=[]
for i in range(len(nums)):
    for n in range(i+1,len(nums)):
        if nums[i]+nums[n]==9:
            ans.append((nums[i],nums[n]))
print(ans)