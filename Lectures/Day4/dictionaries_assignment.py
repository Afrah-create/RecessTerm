shoes = {
    "brand" : "Nike",
    "color" : "black",
    "size" : 10
}

print(f"Shoe size:  {shoes['size']}")

shoes["brand"] = "Adidas"
shoes["type"] = "sneakers"

# printing the keys
for keys in shoes:
    print(keys)

# printing the values
for values in shoes.values():
    print(values)
# check if key "size " exists
for i in shoes:
    if i == "size":
        print("Size exists in the dictionary")


#loop through the dictionary
for key, value in shoes.items():
    print(f"{key} : {value}")
shoes.pop("color")
print(shoes)

# empty the dictionary
shoes.clear()

my_dict = {
    "first_name" : "Awongo",
    "last_name" : "Fahadi",
    "age" : 21,
    "course" : "BSSE"
}

my_dict2 = my_dict.copy()
print(my_dict2)


#nested dicttionary
east_african_countries_info = {
    "country1" : {
        "name" : "Uganda",
        "capital" : "Kampala",
        "population" : 45_000_000
    },
    "country2" : {
        "name" : "Kenya",
        "capital" : "Nairobi",
        "population" : 55_000_000
    },
    "country3" : {
        "name" : "Tanzania",
        "capital" : "Dodoma",
        "population" : 60_000_000
    }
}

for country, info in east_african_countries_info.items():
    print(f"{country}:")
    for key, value in info.items():
        print(f"  {key}: {value}")