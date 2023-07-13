name=input("Hey,Whats your name ")
age=int(input("OK,"+name+" how old are you? "))
if(age<16):
    print(f"You can't drive, {name}")
if(age<18):
    print("Yoi can't vote, ",name)
if(age<25):
    print("You can't rent a car, ",name)
if(age>=25):
    print("You can do anything tht's legal,",name)