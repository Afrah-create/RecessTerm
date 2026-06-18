drinks = set(['Oner','Pepsi', 'Coke'])
# add two more drinks to the set
drinks.add('Minute Maid')
drinks.add('Water')
print(drinks)


myset = {"oven", "kettle", "microwave", "refridgerator"}
if "microwave" in myset:
    print("Microwave is present in the set")

# remove kettle from the set
myset.remove("kettle")
print(myset)

# loop through the set
for i in myset:
    print(i, end=", ")

print("\n")
set1 = {1, 2, 3, 4, 5}
list1 = [4,5]
combined = list1 + list(set1)
print(combined)

my_age = {19, 20, 21}
my_names = {"Awongo"}
my_info = my_age.union(my_names)
print(my_info)