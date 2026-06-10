#cars = [ "Audi", "BMW", "Subaru", "Toyota" ]

#for car in cars:
#    if car == "audi":
#        print(car.upper())
#    else:
#        print(car.title())

#car = "Audi"
#if car == "Audi":
#    print(car.lower())

#name  = "Salam"
#if name != "salam":
#    flag = True
#    print("Your name is not salam")
#else:    print("Your name is salam")

#comparison operators

age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
if age <= 18 and salary >= 500000:
    print("Age and salary criteria met.")
else: print("You do not qualify for the job.")


print("-------------------------------")
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list of fruits.")
else: print("Banana is not in the list of fruits.")