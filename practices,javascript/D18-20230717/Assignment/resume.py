# "edcational_qualifiction":{"sslc":{"school name":"Kumari Matriculation Hr Sec School",
        #                                   "passed year":2017,
        #                                   "percent":87.2},
        #                            "hsc":{"school":"Kumari Matriculation Hr Sec School",
        #                                   "passed year":2019,
        #                                   "percent":58.8},
        #                            "degree":{"college":"DMI Engineering College",
        #                                      "passed year":2023,
        #                                      "percent":63}},

resume={"name":"Abinesh K",
        "email":"abineshk101@gmail.com",
        "mobile no":"7904820356",
        "hardskills":["undergraduated","hindi_learner"],
        "softskills":["leadership","teamworker","sportive_person"],
        "educational qualification":[{"course":"SSLC","institute":"Kumari Matriculation Hr sec school","percentage":87.2,"passed out year":2017},
                                     {"course":"HSC","institute":"Kumari Matriculation Hr sec school","percentage":58.8,"passed out year":2019},
                                     {"course":"BE","institute":"DMI Engineering College","percentage":63,"passed out year":2023}],
        "projects":["smartfarmer_app","sensing moisture","Data saving application"],
        "experience":[{"company":"Wipro","location":"Chennai","years":2,"role":"developer"},
                      {"company":"Karka academy","location":"Nagercoil","years":1,"role":"Teaching Assistant"},
                      {"company":"Tech vip","location":"chennai","years":1,"role":"Training Assistant"}],
        "hobbies":["cricket","listenig music","volleyball"],
        "personal details":{"fathers name":"C.Kumar",
                           "fathers occupation":"cooli",
                           "language known":["Tamil","English"],
                           "dob":"11-09-2001",
                           "gender":"male",
                           "martial status":"No",
                           "address":{"door no":"205/9A",
                                      "compound":"Thanunadar Compound",
                                      "place":"Vattavilai",
                                      "city":"Nagercoil"}}      
        }

for items in resume:
        type1=type(resume[items])
        if type1==str:
                print(items,":",resume[items])
        elif type1==list:
                print(items)
                for info in resume[items]:
                        if type(info)==str:
                                print("\t",info)
                        elif type(info)==dict:
                                for value in info:
                                        print("\t",value,":",info[value])
        elif type1==dict:
                print(items)
                for detail in resume[items]:
                        variable=resume[items][detail]
                        if type(variable)==str:
                                print(detail,":",variable)
                        if type(variable)==list:
                                print(detail)
                                for value in variable:
                                        print("\t",value)
                        if type(variable)==dict:
                                print(detail)
                                for value in variable:
                                        print("\t",value,":",variable[value])


                                


        
