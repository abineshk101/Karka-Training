monthly_goldrate=[{"month":"January","amount":1000},
                  {"month":"February","amount":1200},
                  {"month":"March","amount":1100},
                  {"month":"April","amount":700},
                  {"month":"May","amount":1800},
                  {"month":"June","amount":800},
                  {"month":"July","amount":1250}]
min=[monthly_goldrate[0]["month"],monthly_goldrate[0]["amount"]]
max=[monthly_goldrate[0]["month"],monthly_goldrate[0]["amount"]]
for item in monthly_goldrate:
    if item["amount"]<min[1]:
        min[1]=item["amount"]
        min[0]=item["month"]
    if item["amount"]>max[1]:
        max[1]=item["amount"]
        max[0]=item["month"]
print(f"The minimum gold rate is aquired in the month of {min[0]} at the amount of {min[1]}")
print(f"The maximum gold rate is aquired in the month of {max[0]} at the amount of {max[1]}")