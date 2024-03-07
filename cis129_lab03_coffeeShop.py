#Jorge Camacho
#Coffee Shop Simulator
#Description:

coffee_price = 5.00
muffin_price = 4.00

tax_rate = 0.06


print('***************************************')
print('My Coffee and Muffin Shop')
total_coffees = int(input("Number of coffees bought?\n"))
total_muffins = int(input("Number of muffins bought?\n"))
print('***************************************\n')

subtotal = (total_coffees * coffee_price) + (total_muffins * muffin_price)
tax = subtotal * tax_rate
total = subtotal + tax

print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{total_coffees} Coffee at $5 each: ${total_coffees * coffee_price:.2f}")
print(f"{total_muffins} Muffins at $4 each: ${total_muffins * muffin_price:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")

print("***************************************")

