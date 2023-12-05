mixed_list=[1,2.0,"hai","@",5,6,"&",8,9]
count1=0
for i,real in enumerate(mixed_list):
    value=type(real)
    if value==int or value==float:
        count1+=1
print("The count of real numbers are ",count1)