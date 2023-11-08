nums=[3,2,4,4,3,4,3,1,3,4,3]
for i in range(len(nums)):
    value=0
    a=0
    count=0
    for n in range(len(nums)):
        if nums[i]==nums[n]:
            count+=1
    if count>value:
        value=count
        a=nums[i]
print(a,value)