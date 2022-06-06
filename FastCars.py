#declare variables
speed1 = int()
speed2 = int()
#Get speed1 and speed2
speed1 = int(input("Enter speed:  "))
speed2 = int((input(" Enter speed:  ")))
#Your code goes here.
if (speed1 > 70) and (speed2 > 70):
  print("2 fast cars")
elif (speed1 > 70) or (speed2 > 70):
  print("1 fast car")
else:
  print("no fast cars")