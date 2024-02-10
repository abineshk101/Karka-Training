nums = [3,2,4]
target = 6

def two_sum(nums,target):
    for n in range(len(nums)):
        for l in range(n+1,len(nums)):
            if nums[n]+nums[l]==target:
                print([n,l])
two_sum(nums,target)