from datetime import datetime
current=datetime.today()
ans=current.strftime("%y")  #y define the year number
print(ans)

current=datetime.now()
ans=current.strftime("%Y")  #Y define the year
print(ans)

current=datetime.now()
ans=current.strftime("%m")  #m define the month
print(ans)

current=datetime.now()
ans=current.strftime("%M")  #M define the Minute
print(ans)

current=datetime.now()
ans=current.strftime("%d")  #d define the day
print(ans)

current=datetime.now()
ans=current.strftime("%D")  #D define the Date
print(ans)
 
current=datetime.now().strftime("%T")
print(current)                             #T define the time

