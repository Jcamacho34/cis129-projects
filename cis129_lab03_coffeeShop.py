#Jorge Camacho
#Coffee Shop Simulator
#Description: This program simulates a breakfast shop, allowing the user to input values and purchase products. The program calculates the total price of each item and the final price of your total including tax.

#Defining variables, giving each item a set price.
coffee_price = 5.00
muffin_price = 4.00
scone_price = 2.00
tea_price = 3.00
tax_rate = 0.06

#Prints questions for user and asks number of items purchased.
print('***************************************')
print('My Breakfast Shop')
total_coffees = int(input("Number of coffees bought?\n"))
total_muffins = int(input("Number of muffins bought?\n"))
total_tea = int(input("Number of teas bought?\n"))
total_scones = int(input("Number of scones bought?\n"))
print('***************************************\n')
#Finds subtotal of purchase as well as finds final total including tax.
subtotal = (total_coffees * coffee_price) + (total_muffins * muffin_price) + (total_scones * scone_price) + (tea_price * total_tea)
tax = subtotal * tax_rate
total = subtotal + tax

#prints final receipt, including number of items purchased, their price, and final total including tax.
print("***************************************")
print("My Breakfast Shop Receipt")
print(f"{total_coffees} Coffee at $5 each: ${total_coffees * coffee_price:.2f}")
print(f"{total_muffins} Muffins at $4 each: ${total_muffins * muffin_price:.2f}")
print(f"{total_scones} Scones at $2 each: ${total_scones * scone_price:.2f}")
print(f"{total_tea} Tea at $3 each: ${total_tea * tea_price:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print('Thank you for coming!')
print("***************************************")
