total_bill_amount = float(input("Enter the total bill amount: "))
if total_bill_amount <= 0:
    print("Invalid amount, please enter a number greater than 0.")
    exit()
number_of_people = int(input("How many are you people: "))
if number_of_people <= 0:
    print("Invalid number of people, please enter a number greater than zero.")
    exit()
tip_percentage = float(input("Please enter the tip percentage: "))
if tip_percentage < 0:
    print("Invalid tip percentage, please enter a number greater than or equal to zero.")
    exit()
tip_amount = (tip_percentage / 100) * total_bill_amount
total_amount = total_bill_amount + tip_amount
amount_per_person = total_amount / number_of_people
final_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: UGX {final_amount}")