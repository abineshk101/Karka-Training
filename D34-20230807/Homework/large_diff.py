nums_list=[2,5,8,1,9,3,7]
var1=0
list1=[]
for i in range(len(nums_list)):
    for n in range(len(nums_list)):
        num=nums_list[i]-nums_list[n]
        if num>var1:
            var1=num
            ans=(f"{var1}({nums_list[i]}-{nums_list[n]})")
print(ans)

# def difference(numlist):
#     var1=0
#     for i in range(len(nums_list)):
#         for n in range(len(nums_list)):
#             num=nums_list[i]-nums_list[n]
#             if num>var1:
#                 var1=num
#                 ans=(f"{var1}({nums_list[i]}-{nums_list[n]})")
#     return ans

# nums_list=[2,5,8,1,9,3,7]
# print(difference(nums_list))
