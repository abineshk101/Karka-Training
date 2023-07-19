# name_list=["Abinesh","Dhanush","Ajitha","Abinaya","Sriram"]
# for name in name_list:
#     print(name)

# place_list=[{"name":"Abinesh","place":"Vattavilai","Hobbies":["cricket","music","socialmedia"]},{"name":"Dhanush","place":"Peruvilai","Hobbies":["cricket","football","volleyball"]},{"name":"Ajitha","Place":"Kannangulam","Hobbies":["Aurywork","gardening","readingbooks"]},{"name":"Abinaya","Place":"Vattavilai","Hobbies":["Watching series","Mobile games","movies"]},{"name":"Sriram","place":"Krishnankovil","Hobbies":["cricket","football","mobile games"]}]
# for place in place_list:
#     print(place["Hobbies"])


#                  ////////////         or          ///////////
    

# place_list=[{"name":"Abinesh","place":"Vattavilai","Hobbies":["cricket","music","socialmedia"]},{"name":"Dhanush","place":"Peruvilai","Hobbies":["cricket","football","volleyball"]},{"name":"Ajitha","Place":"Kannangulam","Hobbies":["Aurywork","gardening","readingbooks"]},{"name":"Abinaya","Place":"Vattavilai","Hobbies":["Watching series","Mobile games","movies"]},{"name":"Sriram","place":"Krishnankovil","Hobbies":["cricket","football","mobile games"]}]
# print(place_list[3]["Hobbies"])

# If we need to take element inside of the list which having the dictionaries first take the element in the list using the index of the list 
# and then take the key from the dictionary

# dictionary={"name":"Abinesh","place":"Vattavilai"}
# print(dictionary["name"])

place_list=[{"name":"Abinesh","place":"Vattavilai","Hobbies":["cricket","music","socialmedia"]},
            {"name":"Dhanush","place":"Peruvilai","Hobbies":["cricket","football","volleyball"]},
            {"name":"Ajitha","Place":"Kannangulam","Hobbies":["Aurywork","gardening","readingbooks"]},
            {"name":"Abinaya","Place":"Vattavilai","Hobbies":["Watching series","Mobile games","movies"]},
            {"name":"Sriram","place":"Krishnankovil","Hobbies":["cricket","football","mobile games"]}]
hobby=place_list[1]["Hobbies"]
for i in range(len(hobby)):
    print(hobby[i])

place_list=[{"name":"Abinesh","place":"Vattavilai","Hobbies":["cricket","music","socialmedia"]},{"name":"Dhanush","place":"Peruvilai","Hobbies":["cricket","football","volleyball"]},{"name":"Ajitha","Place":"Kannangulam","Hobbies":["Aurywork","gardening","readingbooks"]},{"name":"Abinaya","Place":"Vattavilai","Hobbies":["Watching series","Mobile games","movies"]},{"name":"Sriram","place":"Krishnankovil","Hobbies":["cricket","football","mobile games"]}]
print(place_list[1]["Hobbies"]) 