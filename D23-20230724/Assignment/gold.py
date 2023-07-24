monthly_goldrate=[{"month":"January","amount":1000},
                  {"month":"February","amount":1200},
                  {"month":"March","amount":1100},
                  {"month":"April","amount":700},
                  {"month":"May","amount":1800},
                  {"month":"June","amount":800},
                  {"month":"July","amount":1250}]
rate_min=monthly_goldrate[0]["amount"]
month_min=monthly_goldrate[0]["month"]
rate_max=monthly_goldrate[0]["amount"]
month_max=monthly_goldrate[0]["month"]
for item in monthly_goldrate:
    if item["amount"]<rate_min:
        rate_min=item["amount"]
        month_min=item["month"]
    if item["amount"]>rate_max:
        rate_max=item["amount"]
        month_max=item["month"]

print(f"The minimum gold rate is aquired in the month of {month_min} at the amount of {rate_min}")
print(f"The maximum gold rate is aquired in the month of {month_max} at the amount of {rate_max}")



    