detail=[{"name":"Abinesh.K","age":21,"place":"Vattavilai"},
        {"name":"Dhanush","age":20,"place":"Suchindram"},
        {"name":"Dhanraj","age":22,"place":"Kottar"},
        {"name":"Bhvanesh","age":23,"place":"Vattavilai"},
        {"name":"Gowtham","age":20,"place":"Parakai"},
        {"name":"Sanjai","age":24,"place":"Vedhanagar"},
        {"name":"Melbin","age":21,"place":"Aral"}]

# for info in detail:
#     print(f'I am {info["name"]},I am {info["age"]} years old and I am from {info["place"]}')

for info in detail:
    if info["age"]>21:
        print(f'I am {info["name"]},I am,{info["age"]} years old,and I am from {info["place"]}')