target=5
a=[1,2,3,4,5]
for i,num in enumerate(a):
    for l,n in enumerate(a) :
        if(n+num==target):
            print("first number= ",num,"index is",i)
            print("second number= ",n,"index is",l)
    
