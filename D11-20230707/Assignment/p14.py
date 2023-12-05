way1=input("Where would you like to go kitchen or upstairs? \n >")
if way1=="kitchen":
    object1=input("Which one would you like to open fridge or cupboard? \n >")
    if object1=="fridge":
        print("Take and eat anything from the fridge")
    elif object1=="cupboard":
        print("Arrange the things in the cupboard")
if way1=="upstairs":
    object1=input("Where you want to go bedroom or hall \n >")
    if object1=="bedroom":
        print("Go and sleep in the bedroom")
    elif object1=="hall":
        print("You can watch the TV")