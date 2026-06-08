total_bill_amount = float(input("Enter the total bill amount: "))
number_of_people = int(input("How many are you people: "))
tip_percentage = float(input("What percentage tip would you like to give? "))
tip_amount = (tip_percentage / 100) * total_bill_amount
total_amount = total_bill_amount + tip_amount
amount_per_person = total_amount / number_of_people
final_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: UGX {final_amount}")