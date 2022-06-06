#declare variables
season = str()
clothing = str()
#Ask the user for the season
season = input("Enter the season:  ")
#Determine proper clothing
if season == "winter":
    clothing = "Heavy Coat"
elif season == "fall":
    clothing = "Sweatshirt"
elif season == "spring":
    clothing = "Jacket"
else:
    clothing = "T-shirt"
#output the proper clothing
print("Based on the season you entered,")
print("you should wear a", clothing)