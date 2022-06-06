#declare variables
Miles = int()
Kilometers = float()

#assign value
Miles = float(input("Miles:  "))

#conversion factor
conv = 1.609344

#Convert miles to kilometers
Kilometers = Miles * conv

print("Kilometers:  ",Kilometers)