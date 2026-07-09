# if 
# Write a if statement that allows a user to enter their age
#  and checks if they are eligible to vote (18 years or older).


# elif
# Extend the previous program to also check if the user is eligible to drive (18 years or older).
# Write if , elif, else statement that allows a user to board a plane to visit a country.
#  The program should check the user's have passport, visa, accommodation, and account balance of $1000
# Code
has_passport = input("Do you have a passport? (yes/no): ").lower()
has_visa = input("Do you have a visa? (yes/no): ").lower()
has_accommodation = input("Do you have accommodation arrangements? (yes/no): ").lower()
account_balance = float(input("Enter your account balance: "))

if has_passport == "yes" and has_visa == "yes" and has_accommodation == "yes" and account_balance >= 1000:
    print("You are eligible to board the plane.")
elif has_passport == "no":
    print("You need a passport to board the plane.")
elif has_visa == "no":
    print("You need a visa to board the plane.")
elif has_accommodation == "no":
    print("You need accommodation arrangements to board the plane.")
elif account_balance < 1000:
    print("You need at least $1000 in your account to board the plane.")
else:
    print("You are not eligible to board the plane.")