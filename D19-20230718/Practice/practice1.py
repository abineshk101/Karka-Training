educational_details=[{"study":"B.Tech",
                      "institute":"Cape",
                      "semester_marks":[{"semester":1,"subjects":["computer program","maths1","Data science"],"semeser_grade":"A"},
                                        {"semester":2,"subjects":["data structure","maths2","network"],"semeser_grade":"B"}]},
                      {"study":"M.Tech",
                      "institute":"Cape",
                      "semester_marks":[{"semester":1,"subjects":["computer program","maths1","Data science"],"semeser_grade":"A"},
                                        {"semester":2,"subjects":["data structure","maths2","network"],"semeser_grade":"B"}]},
                      {"study":"MCA",
                      "institute":"Cape",
                      "semester_marks":[{"semester":1,"subjects":["computer program","maths1","Data science"],"semeser_grade":"A"},
                                        {"semester":2,"subjects":["data structure","maths2","network"],"semeser_grade":"B"}]}
                      ]

for item in educational_details:
    print("\nDegree:")
    print("\t",item["study"])
    for sem in item["semester_marks"]:
        print("Semester:",sem["semester"])
        print("Subjects:")
        for sub in sem["subjects"]:
            print("\t",sub)
        
        