first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
birth_year = int(input("What is your birth year? "))
city = input("What city do you live in? ")
current_year = 2026
age = current_year - birth_year
print(f"You are {first_name} {last_name} and you are {age} years old. And you live in {city}.")