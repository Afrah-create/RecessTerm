'''
has_passport = input("Do you have a passport? (yes/no) ").lower()
has_visa = input("Do you have a visa? (yes/no) ").lower()
paid_amount = float(input("Enter the amount you have paid: "))

if has_passport == "no":
    print("You cannot travel internationally without a passport.")
elif has_visa == "no":
    print("You cannot travel internationally without a visa.")
elif paid_amount < 1000:
    print("You need to pay at least $1000 for international travel.")
else:
    print("You are eligible for international travel. Bon voyage!")

'''

#switch statement
light_color = input("Enter the traffic light color (red/yellow/green): ").lower()
match light_color:
    case "red":
        print("Stop")
    case "yellow":
        print("Caution")
    case "green":
        print("Go")
    case _:
        print("Invalid traffic light color")