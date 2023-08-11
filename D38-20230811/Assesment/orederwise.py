input1=[[1,2,3,[4,5]],[6,7,[8,9]],[10,[11,12,13]]]
for lists in input1:
    for item in lists:
        if type(item)==list:
            for number in item:
                print(number,end=" ")
        else:
            print(item,end=" ")