ready=input("Are you ready for the quiz?,say yes or no ")
if ready=="yes":
    print("Okey,here it comes")
    q1=input("Q10 What is the capital of Alaska? \n \t 1)MElbourne \n \t 2)Anchorage \n \t 3)Juneau \n >")
    if q1=="3":
        print("That's right!")
    elif q1=="1" or q1=="2":
        print("That's wrong!")
    else:
        print("Not defind")
    q2=input("Q2) Can you store the value 'cat' in a variable of type int? \n \t 1)Yes \n \t 2)No \n> ")
    if q2=="2":
        print("That's right")
    elif q2=="1":
        print("Sorry,'cat' is a string. Int can only store numbers.")
    else:
        print("Not defind")
    q3=input("Q3).What is the result of 9+6/3 ? \n \t 1) 5 \n \t 2) 11 \n \t 3) 15/3 \n > ")
    if q3=="2":
        print("That's correct")
    elif q3=="1" or q3=="3":
        print("That's wrong")
    else:
        print("Not defind")
    if q1=="3" and q2=="2" and q3=="2":
        print("Overall,you got 3 out of 3 correct \n Thanks for playing")
    elif q1=="3" and q2=="2" and q3!="2" or q1!="3" and q2=="2" and q3=="2" or q1=="3" and q2!="2" and q3=="2":
        print("Overall,you got 2 out of 3 correct \n Thanks for playing")
    elif q1!="3" and q2!="2" and q3=="2" or q1!="3" and q2=="2" and q3!="2" or q1=="3" and q2!="2" and q3!="2":
        print("Overall,you got 1 out of 3 correct \n Thanks for playing")