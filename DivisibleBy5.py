#declare variable
x = int()

#assign variable
x = 37

#check if divisble by 5, even and positive
if (int(x) % 5 == 0) and (int(x) % 2 == 0) and (int(x) < 0):
      print(str(x) + " is divisble by 5 and even")
else:
  print(str(x) + " is not divisible by 5 or it is odd")


