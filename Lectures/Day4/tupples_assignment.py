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
y.append("infinix")
x = tuple(y)
print("Tuple with new brand: ", x)


