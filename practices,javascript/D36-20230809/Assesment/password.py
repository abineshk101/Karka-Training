def strength(n):
    if n<6:
        return "weak"
    elif 6<=n<=10:
        return "Moderate"
    elif 11<=n<=15:
        return "Strong"
    elif n>15:
        return "Very Strong"

looping=0
while looping<1:
    pswrd=input("Enterpassword ")
    caps=pswrd.isupper()
    small=pswrd.islower()
    ans=False
    if caps==True:
        print("Password must contain atleast one samll letter")
    if small==True:
        print("Password must contain atleast one capital letter")
    for n in pswrd:
        ans=n.isdigit()
        if ans==True:
            break
    if ans==False:
        print("Password must contain atleast one number")
    if caps==False and small==False and ans==True:
        print(f"Your password is {strength(len(pswrd))}")
        looping=1
                                                                                            # for n in pswrd:
                                                                                            #     try:
                                                                                            #         int(n)
                                                                                            #         ans=True
                                                                                            #         break
                                                                                            #     except:
                                                                                            #         ans=False

#




        