from datetime import datetime
from datetime import timedelta

date_str="26 July 2023"
objct=datetime.strptime(date_str,"%d %B %Y")
value_date=objct+timedelta(minutes=1)
print(value_date)
