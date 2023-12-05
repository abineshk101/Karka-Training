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

