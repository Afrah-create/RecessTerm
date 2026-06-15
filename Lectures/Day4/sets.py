'''
cars = {"Toyota", "Honda", "Ford"}
print(cars)
print(type(cars))

# demonstrating unique values in a set
numbers = {"Awongo", 1, 2, 3, 4, 5, 1, 2, 3}
print(numbers)

# accesing an element in a set
if "Awongo" in numbers:
    print("Awongo is present in the set")

# adding an element to a set
numbers.add(6)
numbers.add("Afrah")
print(numbers)

# removing an element from a set
numbers.remove(6)
print(numbers)

'''

user_names = {"Awongo", "Afrah", "Aisha"}
email_addresses = {"awongo@gmail.com", "afrah@gmail.com", "aisha@gmail.com", "Awongo"}

user_info = user_names.union(email_addresses)
print(user_info)

intersection = user_names.intersection(email_addresses)
print(intersection)

# adding multiple elements to a set
user_names.update(["Hassan", "Abdi"])
print(user_names)