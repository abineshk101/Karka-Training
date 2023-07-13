def add_keychains():
    return ("ADD KEYCHAINS \n")

def remove_keychains():
    return ("REMOVE KEYCHAINS \n")

def view_order():
    return ("VIEW ORDER \n")

def checkout():
    return ("CHECKOUT")

print("Keychain shop")
user=0
while user<4:
    print("1.Add ketchains to  order \n2.Remove keychain from the order \n3.View current order \n4.Checkout")
    user=int(input("Please enter your choice: "))
    if user==1:
        print(add_keychains(),"\n")
    if user==2:
        print(remove_keychains(),"\n")
    if user==3:
        print(view_order(), "\n")
    if user==4:
        print(checkout())