name=input("Hey,Whats your name ")
age=int(input("OK,"+name+" how old are you? "))
if(age<16):
    print("You can't drive, ",name)
elif(16<=age<18):
    print("You can drive but not vote, ",name)
elif(18<=age<25):
    print("You can vote but not rent a car, ",name)
else:
    print("You can do pretty much anything ,",name)