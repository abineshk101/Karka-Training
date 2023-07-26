from datetime import datetime

date_str="26 July 2023"
objct=datetime.strptime(date_str,"%d %B %Y")
print(objct)