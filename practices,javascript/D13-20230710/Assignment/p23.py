n3=0
n5=0
n3_n5=0
for n in range(1,101):
    if n%3==0:
        n3=n3+1
        print("Fizz")
    if n%5==0:
        n5=n5+1
        print("Buzz")
    if n%3==0 and n%5==0:
        n3_n5=n3_n5+1
        print("FizzBuzz")
print(f"count of number divisible by 3 is {n3} \ncount of number divisible by 5 is {n5} \ncount of number divisible by 3 and 5 is {n3_n5}")