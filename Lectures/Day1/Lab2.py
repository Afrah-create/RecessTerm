
yob = int(input("Please enter your year of birth: "))
current_year = 2026
age = current_year - yob
print("You are " + str(age) + " years old.")

if(age >= 18):
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")
