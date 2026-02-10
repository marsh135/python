"""
meal =  float(input("How much did the meal cost:  "))
tax = meal *.1
tip = float(input("What percentage of a tip would you like to add? "))
tipPercent =  tip/100
totalTip =  meal*tipPercent
totalBill = meal+tax+totalTip
print(f"Meal cost: ${meal:.2f}   Tax: ${tax:.2f}   Tip: ${totalTip:.2f}    Total: ${totalBill:.2f}")


print("Meat cost: $"+str(meal))
print("Tax: $"+str(round(tax)))
print("Tip: $"+str(round(totalTip)))
print("Total: $"+str(round(totalBill)))
"""

"""


#Part 3
partySize =  int(input("How many people are in your group? "))
prices =[0]
tips = [0]
for i in range(1,partySize+1):
  meal = float(input(f"How much is the meal for person {i}? "))
  prices.append(meal)

tip = float(input(f"Enter the tip percentage for person: "))
tPrice = 0
tTip = 0
for i in prices:
  tPrice+=i

tTip =  tPrice * (tip/100)
individualShare =  (tPrice+tTip+(tPrice/10))/(len(prices)-1)


print(f"Meal: ${tPrice:.2f}    \nTip: ${tTip:.2f}    \n\nTotal:${tPrice+tTip:.2f}    \nIndividual Share: ${individualShare:.2f}")




"""
#part 4
partySize =  int(input("How many people are in your group? "))
prices =[0]
tips = [0]
for i in range(1,partySize+1):
  meal = float(input(f"How much is the meal for person {i}? "))
  print(f"After Tax: ${meal*1.1:.2f}")
  prices.append(meal*1.1)
  tip = float(input(f"Enter the tip percentage for person {i}: "))
  tips.append(meal*(tip/100))

print("-"*20)
for i in range(1, len(prices)):
  print(f"Person {i} owes ${prices[i]+tips[i]:.2f}.")
  print(f"Meal: ${prices[i]:.2f}  Tax:  ${prices[i]*.1:.2f}     Tip: ${tips[i]:.2f}")
  print("-"*20)


