gender=input("What is your gender? (male or female): ")
frst_name=input("First name: ")
lst_name=input("Last name: ")
age=int(input("Age: "))
mrg=input(f"are you married,{frst_name}: ")
if gender=="male":
    if age>=20:
        print(f"Mr.{frst_name}{lst_name}")
    else:
        print(frst_name,lst_name)
elif gender=="female":
    if age>=20 and mrg=="yes":
        if age>=20 and mrg=="yes":
             print(f"Mrs.{frst_name}{lst_name}")
    elif age<20 and mrg=="no" or age>=20 and mrg=="no":
        print(f"Ms.{frst_name}{lst_name}")