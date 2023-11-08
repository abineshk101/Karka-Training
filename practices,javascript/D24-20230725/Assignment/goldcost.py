monthly_goldrate=[{"month":"JANUARY",
                   "amount":1000,
                  "jwel":[{"name":"CHAIN","making_cost":12},{"name":"EARING","making_cost":15}]},
                  {"month":"FEBRUARY",
                  "amount":1200,
                  "jwel":[{"name":"CHAIN","making_cost":18},{"name":"EARING","making_cost":13}]},
                  {"month":"MARCH",
                  "amount":1100,
                  "jwel":[{"name":"CHAIN","making_cost":15},{"name":"EARING","making_cost":11}]},
                  {"month":"APRIL",
                  "amount":700,
                  "jwel":[{"name":"CHAIN","making_cost":17},{"name":"EARING","making_cost":12}]}]

# for detail in monthly_goldrate:
#     print("\nMonth:",(detail["month"]),"\nGold rate:",detail["amount"])
#     for amount in detail["jwel"]:
#         print("\tJewel name:",amount["name"],"\n\tMaking cost",amount["making_cost"],"%")
#         total=(amount["making_cost"]/100)*detail["amount"]+detail["amount"]
#         print("The amount for {}".format(amount["name"]),total)


for detail in monthly_goldrate:
    dictionary={}
    dictionary["month"]=detail["month"]
    dictionary["gold_detail"]=detail["amount"]
    gold_items=[]
    for amount in detail["jwel"]:
        dictionary2={}
        total=(amount["making_cost"]/100)*detail["amount"]+detail["amount"]
        dictionary2["item"]=amount["name"]
        dictionary2["Amount"]=total
        gold_items.append(dictionary2)
    dictionary["gold_items"]=gold_items
    print(dictionary)
