x = ("samsung", "apple", "tecno", "redmi")
print("My favorite brand: ", x[0])


print("Second last brand: ", x[-2])

#modifying a tuple
y = list(x)
y[1] = "itel"
x = tuple(y)

print("Modified tuple: ", x)

# adding a new element to the tuple
y = list(x)
y.append("Huawei")
x = tuple(y)
print("Tuple with new brand: ", x)


number_of_brands = len(x)
print("Number of brands: ", number_of_brands)

for i in range(number_of_brands):
    print(x[i], end=", ")


# remove first element from the tuple

y = list(x)
y.remove(y[0])
x = tuple(y)
print("Tuple after removing first element: ", x)

cities = tuple(["Kampala", "Arua", "Gulu", "Mbale", "Mbarara", "Entebbe", "Fort Portal"])
print("Cities: ", cities)

# unpacking the cities tuple
city1, city2, city3, city4, city5, city6, city7 = cities
print("City 1: ", city1)
print("City 2: ", city2)
print("City 3: ", city3)
print("City 4: ", city4)
print("City 5: ", city5)
print("City 6: ", city6)
print("City 7: ", city7)

print("2nd, 3rd and 4th cities: ", cities[1:4])

first_name = ("Awongo")
last_name = ("Fahadi", "Rashid")
full_name = first_name + " " + last_name[0] + " " + last_name[1]
print("Full name: ", full_name)


color = ("red", "green", "blue", "yellow", "orange")
colors = color * 3
print("Colors: ", colors)

thistuple = (1,3,7,8,7,5,4,6,8,5)
print(f"Eight appears {thistuple.count(8)} times in the tuple.")

