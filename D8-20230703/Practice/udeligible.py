def elig(year):
    eligible=year>=2021
    return eligible

yr=int(input("enter the year"))
year=elig(yr)
print(year)

