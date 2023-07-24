name=input("Enter your name: ")
input_list=input("Enter the units in order with the use of (,)")
a=(input_list.split(','))
list1=[]
data={}

for n in a:
    interger=int(n)
    list1.append(interger)
print(list1)
