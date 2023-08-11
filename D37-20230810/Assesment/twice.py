nums=[1,2,4,1,2]
ans=nums[1]
for n in nums:
    if nums.count(n)<2:
        ans=n
print(ans)