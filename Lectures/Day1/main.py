def get_tip_percentage():
    print("\nTip options:")
    print("1. 10%")
    print("2. 15%")
    print("3. 20%")
    print("4. Custom")
    
    while True:
        choice = input("Choose tip option (1-4): ").strip()
        if choice == '1':
            return 10
        elif choice == '2':
            return 15
        elif choice == '3':
            return 20
        elif choice == '4':
            while True:
                try:
                    custom = float(input("Enter custom tip percentage: "))
                    if custom < 0:
                        print("Tip percentage cannot be negative.")
                    else:
                        return custom
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    print("=" * 40)
    print("      BILL SPLIT CALCULATOR")
    print("=" * 40)

    # Get total bill amount
    while True:
        try:
            bill_amount = float(input("\nEnter total bill amount: "))
            if bill_amount <= 0:
                print("Bill amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get number of people
    while True:
        try:
            num_people = int(input("Enter number of people: "))
            if num_people <= 0:
                print("Number of people must be at least 1.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Get tip percentage
    tip_percent = get_tip_percentage()

    # Calculations
    tip_amount = (tip_percent / 100) * bill_amount
    total_bill = bill_amount + tip_amount
    amount_per_person = total_bill / num_people

    # Output formatted receipt
    print("\n" + "=" * 40)
    print("            RECEIPT")
    print("=" * 40)
    print(f"  Bill Amount:       ${bill_amount:.2f}")
    print(f"  Tip ({tip_percent}%):        ${tip_amount:.2f}")
    print(f"  Total Bill:        ${total_bill:.2f}")
    print(f"  Number of People:  {num_people}")
    print("-" * 40)
    print(f"  Each Person Pays:  ${amount_per_person:.2f}")
    print("=" * 40)


if __name__ == "__main__":
    main()