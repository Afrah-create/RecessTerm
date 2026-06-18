# lamda functions
# lamda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not worth defining with a full function definition.
# Lab1: simple lamda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3)) 


def add(x, y):
    return x + y
print(add(5, 3))


check_even = lambda x: x % 2 == 0
print(check_even(4))


numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


number = [34,52,12,90,34,21, 67, 89, 23, 45]
# Using lambda function to sort the list in ascending order
sorted_numbers = sorted(number, key=lambda x: x, reverse=True)
print(sorted_numbers)


fruits = ["Cherry", "Banana", "Date", "Apple", "Mango", "Dragonfruit"]
fruits.sort(key=lambda x: len(x))
print(fruits)