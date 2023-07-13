marks=[3,2,4,1,3]
tot_marks=0
enum_marks=enumerate(marks)
print(type(enum_marks))
for i,mark in enumerate(marks):
    print("entering iteration process item",i)
    print("Before sum ",tot_marks)
    tot_marks=tot_marks+mark
    print("after sum",tot_marks)
    print("Exiting iteration process for item",i)
    print("\n")

