print("\n\nDictionary demonstration")
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
#print(data)


account = dict(
    username="afrah",
    email="afrah@gmail.com",
    password="123456"
)

# adding to a dictionary
account["age"] = 25
account["district"] = "Obongi"

print(account)

age = account.pop("age")
print("Removed age:", age)
print("Updated account:", account)

# deleting a key-value pair
del account["district"]
print("Account after deleting district:", account)

print("Iterating through dictionary:")
for key, value in account.items():
    print(f"{key}: {value}")

