amount=[100,180,260,300,700,55,600]
least_amnt=amount[0]+1
high_amnt=0
buying_day=None
selling_day=None
for i in range(len(amount)):
    if amount[i]<least_amnt:
        least_amnt=amount[i]
        buying_day=i+1
        for n in range(i,len(amount)):
            if amount[n]>high_amnt:
                high_amnt=amount[n]
                selling_day=n+1

profit=high_amnt-least_amnt
print(f"The customer bought the product on {buying_day} and sold it on {selling_day}.The profit is {profit}")
