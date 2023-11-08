input1=[1,100,300,4]

def large(input1):
    value=input1[0]
    # Method 1 ////////////
    for num in input1:
        if(num>value):
            value=num
    return value

    # Method : 2 ////////////
    # for i in range(1,len(input1)):
    #     if(input1[i]>value):
    #         value=input1[i]  
    # return value

    # Method : 3 /////////////
    # for i in input1[1:]:
    #     if(i>value):
    #         value=i  
    # return value

print("The large number is",large(input1))
