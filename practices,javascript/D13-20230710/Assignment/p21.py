height=float(input("Your height in meter: "))
weight=float(input("Your weight in kg: "))
bmi=weight/height**2
print(f"Your BMI is: {bmi}")
if bmi<18.5:
    print("BMI Category:underweight")
elif 18.5<=bmi>=24.9:
    print("BMI Category:normal weight")
elif 25.0<=bmi>=29.5:
    print("BMI Category:overweight")
elif bmi>=30.0:
    print("BMI Category:obese")
