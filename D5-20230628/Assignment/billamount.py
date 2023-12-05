chicken=150.85
mutton=320.777
beaf=270.33
veg=110.85
total=chicken+mutton+beaf+veg
print("Total cost: ",total)
print("GST percentage: 18%")
gst=total+(total*18/100)
print("Include GST: ",gst)

# total is got by adding all items using "+" operator
# GST percentage is showed
# gst is calculated by dividing GST percentage by 100 using "/" operator and multiplied with total using "*" operator
# total amount is added with gst amount using "+" operator 