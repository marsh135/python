class menu:
    def __init__(self, item, cost, id):
        self.item = item
        self.cost =  cost
        self.id =  id
    def __str__(self):
        return f"{self.id}  - {self.item}, {self.cost}"

cb = menu("Cheeseburger", 5.99, 1)
hb = menu("Hamburger", 4.99, 2)
fries =  menu("Fries", 1.99, 3)
drink = menu("Drink", 1.29, 4)
cC = menu("Corn Casserole", 9.99, 5)

items =  [cb.item, hb.item, fries.item, drink.item, cC.item]
costs =  [cb.cost, hb.cost, fries.cost, drink.cost, cC.cost]
id = [cb.id, hb.id, fries.id, drink.id, cC.id]


for i in range(0, len(items)):
    print(f"{id[i]}: {items[i]},${costs[i]}")
