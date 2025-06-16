cost_price = float(input("enter the cost price:"))
sell_price = float(input("enter the selling price:"))

if (cost_price > sell_price):
    loss= cost_price - sell_price
    print("the seller has made a loss, Amount of loss is: ", loss )
    
elif(sell_price > cost_price):
    profit= sell_price - cost_price
    print("the seller has made profit, Amount of profit is: ", profit)
    
else:
    print("the seller has neither made profit or loss")

if profit <= 50:
    tax= profit*0.02
elif (profit>51 and profit < 100):
    tax= profit*0.04
elif (profit>=100 and  profit<500):
    tax= profit*0.05
else:
    tax= profit*0.07
    
final_amount= profit - tax
print("the amount left after deduction of taxes is: ", final_amount)
