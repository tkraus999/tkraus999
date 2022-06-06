#declare variables
num_doughnuts = int()
price = float()
subtotal = float()
tax = float()
total = float()
#Ask user for the number of doughnuts
num_doughnuts = int(input("Enter the number of doughnuts:  "))
#Determine price for each doughnut
if num_doughnuts <= 6:
    price = 1.5
elif num_doughnuts <= 8:
    price = 1.25
elif num_doughnuts <= 12:
    price = 1.15
else:
    num_doughnuts > 13
    price = 1.00
#Determine the tax, subtotal and total
subtotal = num_doughnuts * price
tax = subtotal * 0.06
total = subtotal + tax

#print out subtotal, tax and total
print("Subtotal:  $", subtotal)
print("Tax:  $", tax)
print("Total:  $", total)