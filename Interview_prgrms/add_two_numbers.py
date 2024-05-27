
def add_two_number(l1,l2):
    num1=""
    num2=""
    ansList=[]
    for i in range(len(l1)):
        num1=str(l1[i])+num1
        num2=str(l2[i])+num2
    ans=str(int(num1)+int(num2))
    for i in range(len(ans)):
        ansList.append(int(ans[i]))
    return ansList

l1 = [2,4,3]
l2 = [5,6,4]
print(add_two_number(l1,l2))






