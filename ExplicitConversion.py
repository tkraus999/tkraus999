#declare variables
quantity = int()
product = str()
new_string = str()

#assign value to variables
quantity = 5
product = "pencil"
num1 = 4
num2 =5.5

#explicit conversion of quantity to a string
new_string=product + ": " + str(quantity)

#explicit conversion of the sum to supress (truncate) the decimal value
sum = num1 + num2
sum = int(sum)

#printing new string and sum
print(new_string)
print(sum)