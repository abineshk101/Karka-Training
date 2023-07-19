items_list = [{'name':'Apple','category':'Fruits'},
              {'name':'Carrot','category':'Vegetables'},
              {'name':'Banana','category':'Fruits'},
              {'name':'Broccoli','category':'Vegetables'}]
fruits=[]
vegetables=[]
for value in items_list:
    if value["category"]=="Fruits":
        fruits.append(value["name"])
    if value["category"]=="Vegetables":
        vegetables.append(value["name"])
print({"Fruits":fruits,"Vegetables":vegetables})


                        # /////////// or ///////////// #

# fruits=[]
# vegetables=[]
# food={}
# for value in items_list:
#     if value["category"]=="Fruits":
#         fruits.append(value["name"])
#     if value["category"]=="Vegetables":
#         vegetables.append(value["name"])
# food["Vegetables"]=vegetables
# food["Fruits"]=fruits
# print(food)

        