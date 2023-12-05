class_list=["Tamil","English","Maths","Science","Social"]
teach_list=["Subin","Kavin","Dev","Raj","Sujin"]
print("+"+"-"*41+"+")
for n in range(len(teach_list)):
    # print(class_list[i],teach_list[i])
    print('|{}| {:>20} | {:>14} |'.format(n+1,class_list[n],teach_list[n]))
print("+"+"-"*41+"+")


