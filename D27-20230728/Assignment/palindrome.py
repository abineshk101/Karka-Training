# string="level"
# ans=""
# for n in string:
#     ans=n+ans
# if ans==string:
#     print(True)
# else:
#     print(False)

# string="malayalam"
# for i in range(len(string)):
#     if string[i]==string[len(string)-(i+1)]:
#         print(True)
#         break
#     else:
#         print(False)
#         break

string="level"
new_string=""
for i in range(len(string)-1,-1,-1):
    new_string=string[i]+new_string
if new_string==string:
    print(True)
else:
    print(False)