sentence="hellowworld"
count={}
for n in sentence:
    if n in count.keys():
        count[n]=count[n]+1
    else:
        count[n]=1
print(count)