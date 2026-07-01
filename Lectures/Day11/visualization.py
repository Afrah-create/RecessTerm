import matplotlib.pyplot as plt
'''
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,5,7,11,13,17,19,23,29]


fig, ax = plt.subplots()
ax.set_facecolor('lightgray')

ax.plot(x, y, marker='o', linestyle='-', color='b')
ax.set_title("Prime Numbers")
ax.set_xlabel("Index")
ax.set_ylabel("Prime Number Value")
#plt.show()


names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
age = [25, 30, 35, 40, 45]
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.bar(names, age, color='green')
ax.set_title("Age of Individuals")
ax.set_xlabel("Names")
ax.set_ylabel("Age")
plt.show()


# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.hist(data, bins=5, color='purple', edgecolor='black')
ax.set_title("Histogram of Data")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
plt.show()

# Pie Chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [15, 30, 45, 10]
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'pink', 'brown'])
ax.set_title("Fruit Distribution")

plt.show()

# Box Plot
data = [[7, 8, 5, 6, 9, 10, 12, 15, 14, 13], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
fig, ax = plt.subplots()
ax.set_facecolor('lightgray')
ax.boxplot(data, patch_artist=True, boxprops=dict(facecolor='cyan', color='blue'), medianprops=dict(color='red'))
ax.set_title("Box Plot of Data")
ax.set_ylabel("Values")
plt.show()
'''

# Heatmap
import seaborn as sns
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
fig, ax = plt.subplots()
sns.heatmap(x, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
ax.set_title("Heatmap of Matrix")
plt.show()