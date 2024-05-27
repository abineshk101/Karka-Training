def max_num(aray):
    
    max_number=  0
    second_max = 0

    for n in aray:
        if n > max_number:
            second_max = max_number
            max_number = n
        elif n > second_max:
            second_max = n

    return second_max

aray = [10,27,6,1,2]
print(max_num(aray))