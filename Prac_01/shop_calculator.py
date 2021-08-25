cost = []
number_of_items = int(input("Enter the number of items : "))
for i in range (1, number_of_items+1):
    price_of_item = float(input("price of item: $"))
    cost.append(price_of_item)
full_amount = sum(cost)
if full_amount > 100:
    new_amount = full_amount - (full_amount* 0.10)
    print("Total price for", (number_of_items), "items is :$""{:.2f}".format(new_amount))
else:
    print("Total price for", (number_of_items), "items is :$""{:.2f}".format(full_amount))



