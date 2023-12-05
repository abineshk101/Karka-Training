# n=5
# num=1
# for i in range(n):
#     for k in range(n):
#         print(num,end=" ")
#         num=num+1
#     print("")

n=5
for i in range(1,n*n+1):
    print(i,end=" ")
    if i%n==0:
        print('')