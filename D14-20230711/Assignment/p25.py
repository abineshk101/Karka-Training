list1=["January","February","March","April","May","June","July","August","September","October","November","December"]
def month(num):
    for i,n in enumerate(list1):
        if num==i+1:
            return (n)
num=int(input("Enter the month number "))       
print(month(num))
   
