print("Think number between 1-100")
num=50
for n in range(7):
    guess=int(input(f"guess {n+1}: "))
    if n<6:
        if guess==50:
            print("You are correct")
            break
        elif guess>num:
            print("It is too large")
        elif guess<num:
            print("It is too small")
    else:
        print("You exeed the limit")
