def vow_count(list1):
    count=0
    vowels=['a','e','i','o','u']
    for n in vowels:
        if n in list1:
            count=count+1
    return count
        
maxi=0
name=""
string="Hai I'm Niranjan and Im from Nagercoil"
list1=string.lower().split(" ")
for value in list1:
    if vow_count(value)>maxi:
        maxi=vow_count(value)
        name=value
print(name)

