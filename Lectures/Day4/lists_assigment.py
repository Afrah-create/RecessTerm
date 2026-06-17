items = list([1,2,3,4,5])
print(f"Second item: {items[1]}")

items[1] = 0
print(f"After change: {items}")

items.append(6)
print(f"After adding a sixth item: {items}")


items.insert(2, "Bathel")
print(f"After inserting a new item: {items}")

items.remove(3)
print(f"After removing the fourth item: {items}")

total_items = len(items)
print(f"Length of the list: {total_items}")


print(f"Last item: {items[-1]}")

new_list = list([7,8,9,10,11,12,13])
print(f"New list: {new_list}")
print(f"Third to fifth items: {new_list[2:5]}")

countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
print(f"Countries: {countries}")

countries_copy = countries.copy()
print(f"Copied Countries: {countries_copy}")

for i in countries:
    print(i, end=", ")

print("\n")
animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger"]
# ascending order
animals.sort()
print(animals)
# descending order
animals.sort(reverse=True)
print(animals)

for i in animals:
    if "a" in i:
        print(i, end=", ")


first_name = ["Awongo", "Fahadi"]
second_name = ["Rashid"]
print("\n" + " ".join(first_name + second_name))