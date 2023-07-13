n=[1,2,3,4,5,6,7,8,9]
odd_count=0
even_count=0
trip_count=0
for i,num in enumerate(n):
    if (num%2)==0:
        even_count=even_count+1 
    if(num%3)==0:
        trip_count=trip_count+1                  #even_count+=1           
    if(num%2)!=0:
        odd_count=odd_count+1 
                       # here we can also use else statement
print("The odd number count is ",odd_count)
print("The even number count is ",even_count)
print("The triple number count is ",trip_count)

        
