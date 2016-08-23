class Food():
    # This defines a food object that we can store various attributes for
    def __init__(self, name, quantity, location, unit_price, box_qty, purchase_price_box):
        self.name = name
        self.quantity = quantity # number on hand
        self.location = location
        self.unit_price = unit_price
        self.box_qty = box_qty
        self.purchase_price_box = purchase_price_box

    def profit(self):
        # a method to return the profit on selling all the items in a box, it takes a food item as its argument
        # first, multiply the sale price by the number of items in a box.
        sales = self.unit_price * self.box_qty
        # then, subtract the per box price from this total to find the profit for one box
        box_profit = sales - self.purchase_price_box
        # eventually, multiply this by the total number of boxes to get total potential profit
        total_profit = box_profit * self.quantity
        # and return the total profit
        return total_profit

# eventually we want to calculate the potential profit from the food items we have on hand.

# let's test Food object
coke = Food("Coca-Cola", 3, "aisle 2", 1.45, 24, .25)
rice = Food("rice", 10, "aisle 2", 20.89, 40, 18)
pasta = Food("pasta", 20, "aisle 2", 1.78, 30, 8.56)
beans = Food("beans", 12, "aisle 2", 5.29, 14, 3.50)
milk = Food("milk", 4, "aisle 2", 2.46, 20, 1.00)
oil = Food("oil", 2, "aisle 2", 4.43, 18, 2.16)

# store our items in an inventory,  let's use a list for now...
inventory = [coke,rice,pasta,beans, milk, oil]

# print(beans.name + "sell for $" + str(coke.unit_price)) + " each."
# print("Which means we have a potential profit of " + beans.profit() + " for all the beans in stock.")

for item in inventory:
    print (item.name + " is in " + item.location + " and sells for $" + str(item.unit_price) + " each.")

print ("\nthe profit ")
# let's print out profit for our items and then print a grand total
net_profit = 0
for item in inventory:
    print (item.name + " $" + str(item.profit()))
    net_profit += item.profit()

print("\nGrand total profit is $" + str(net_profit))