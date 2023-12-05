user=[{"name":"vimal",
       "mail":"vimal@gmail.com","password":"vimal123",
       "hobbies":["music","youtube","cricket"],"frds_list":["abi","arun","karan"]},
      {"name":"arav",
      "mail":"arav@gmail.com","password":"arav123",
      "hobbies":["socialmedia","football","cricket"],"frds_list":["karan","abi","das"]},
      {"name":"arjun",
      "mail":"arjun@gmail.com","password":"arjun123",
      "hobbies":["reading","volleyball","watcing_tv"],"frds_list":["bhuvi","raj","gowtham"]},
      ]

dictionary={}
info=input("Please choose the option\n\t1)create an account\n\t2)login existing account\n>")
if info=="1":
    nme=input("Your name: ")
    e_mail=input("Create your id: ")
    pss=input("Create your own password: ")
    hby=input("Your hobbies: ")
    frnd=input("Your friends list: ")
    list1=hby.split(",")
    list2=frnd.split(",")
    dictionary["name"]=nme
    dictionary["mail"]=e_mail
    dictionary["hobbies"]=hby
    dictionary["frds_list"]=frnd
    print(dictionary)
    user.append(dictionary)

elif info=="2":
    def take(list1):
        for n in list1:
            print(n)

    email=input("Enter your email id: ")
    pswrd=input("Enter your password: ")

    for value in user:
        if value["mail"]==email and value["password"]==pswrd:
            value["loggedIn"]=True
            print("\nYour hobbies are:\t")
            take(value["hobbies"])
            print("\nYour friends are")
            take(value["frds_list"])
        else:
            value["loggedIn"]=False
print(user)