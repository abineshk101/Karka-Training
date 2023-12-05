players=[{"name":"Flintoff","country":"England","centuries":8,"half centuries":26,"wickets":226,"hatrick":8,"topscore":167},
         {"name":"Jacques Kallis","country":"South Africa","centuries":45,"half centuries":149,"wickets":292,"hatrick":4,"topscore":224},
         {"name":"Kapil Dev","country":"India","centuries":9,"half centuries":42,"wickets":687,"hatrick":12,"topscore":175},
         {"name":"Sanath Jayasuriya","country":"Srilanka","centuries":42,"half centuries":103,"wickets":451,"hatrick":3,"topscore":340},
         {"name":"Shakib Al Hasan","country":"Bangladesh","centuries":14,"half centuries":98,"wickets":327,"hatrick":6,"topscore":217}]
temp=[players[0]["name"],players[0]["topscore"]]
# player_name=players[0]["name"]
print("Players scored more than 10 centuries from the above list:")
for cricketer in players:
    if  cricketer["centuries"]>10:      
        print("\t",cricketer["name"])

print("Players taken more than 5 hatricks from the above list:")
for cricketer in players:
    if  cricketer["hatrick"]>5:      
        print("\t",cricketer["name"])

print("Player who scored highest runs from the above list:")
for cricketer in players[1: ]:
    if cricketer["topscore"]>temp[1]:
        temp[1]=cricketer["topscore"]
        temp[0]=cricketer["name"]
print("\t",temp[0],temp[1])






        