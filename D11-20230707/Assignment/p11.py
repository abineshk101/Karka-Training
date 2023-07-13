def wght(weight,n):
    if n==1:
        return weight*0.78
    elif n==2:
        return weight*0.39
    elif n==3:
        return weight*2.65
    elif n==4:
        return weight*1.17
    elif n==5:
        return weight*1.05
    elif n==6:
        return weight*1.23

weight=int(input("Please enter your current weight: "))
print("I have information for the following planets \n \t 1.Venus  2.Mars  3.Neptune \n \t 4.Saturn 5.Uranus 6.Neptune")
n=int(input("Which planet you are visiting "))
print("Your weight would be ",wght(weight,n)," on that planet")