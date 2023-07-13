first_name=input("First name: ")
last_name=input("Last name: ")
grade=input("Grade (1-10): ")
id=input("Student ID: ")
login=input("Login ID: ")
gpa=input("GPA (0.0-5.0): ")

# print("Your information: ")
# print("\t Name:          "+first_name,last_name)
# print("\t Login ID:      ",login)
# print("\t Student ID:    ",id)
# print("\t GPA:           ",gpa)
# print("\t Grade:         ",grade)


# print("Your information: \n \t Name: "+first_name,last_name ,"\n \t Login ID: ",login,"\n \t Student ID: ",id,"\n \t GPA: ",gpa,"\n \t Grade: ",grade)

print("Your information: \n \t Name: {:>9} \n \t Login ID: {:>5} \n \t Student ID: {:>3} \n \t GPA: {:>10} \n \t Grade: {:>8}" .format(first_name+last_name,login,id,gpa,grade))