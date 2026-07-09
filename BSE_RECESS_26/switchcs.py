
# Multiple patterns in one case
light_color = input("Enter the traffic light color (red, yellow, green): ").lower()

match light_color:
    case "red" | "yellow":
        print("Stop!")
    case "green":
        print("Go!")
    case _:
        print("Invalid traffic light color.")


# Exe2: write a  program that uses a switch-case structure to determine
# day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.)
#  and prints the corresponding day name.