string="the quick brown fox jumps over the lazy dog the quick brown fox"
list1=string.split()
sum=[]
dictionary={}
for i in range(len(list1)):
    if list1[i] not in sum:
        b=sum.append(list1[i])
for n in sum:
    dictionary[n]=list1.count(n)
print(dictionary)
        

