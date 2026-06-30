'''
Numpy array functions
Provide a wide range of functions to perform operations on arrays. Some of the commonly used functions include:
1. np.sum(): Computes the sum of array elements.
2. np.mean(): Computes the mean of array elements.
3. np.std(): Computes the standard deviation of array elements.
4. np.min(): Finds the minimum value in the array.
5. np.max(): Finds the maximum value in the array.
6. np.reshape(): Reshapes the array to a specified shape.
7. np.transpose(): Transposes the array (swaps rows and columns).
8. np.concatenate(): Concatenates two or more arrays along a specified axis.
9. np.unique(): Finds the unique elements in the array.
10. np.sort(): Sorts the array elements in ascending order.
11. np.argmin(): Returns the index of the minimum value in the array.
12. np.argmax(): Returns the index of the maximum value in the array.


'''

import numpy as np

array_1 = np.array([1, 2, 3, 4, 5])
# Sum of array elements
sum_array_1 = np.sum(array_1)
print("Sum of array_1 elements:", sum_array_1)

# Mean of array elements
mean_array_1 = np.mean(array_1)
print("Mean of array_1 elements:", mean_array_1)

# Standard deviation of array elements to 3 decimal places
std_array_1 = np.std(array_1)
print("Standard deviation of array_1 elements:", round(std_array_1, 3))

# Minimum value in the array
min_array_1 = np.min(array_1)
print("Minimum value in array_1:", min_array_1)

# Maximum value in the array
max_array_1 = np.max(array_1)
print("Maximum value in array_1:", max_array_1)

# Unique elements in the array
unique_array_1 = np.unique(array_1)
print("Unique elements in array_1:", unique_array_1)

# Sorted elements in the array
sorted_array_1 = np.sort(array_1)
print("Sorted elements in array_1:", sorted_array_1)

# Index of the minimum value in the array
argmin_array_1 = np.argmin(array_1)
print("Index of minimum value in array_1:", argmin_array_1)

# Index of the maximum value in the array
argmax_array_1 = np.argmax(array_1)
print("Index of maximum value in array_1:", argmax_array_1)

# Reshaping the array to a 2x3 shape
reshaped_array_1 = np.reshape(array_1, (2, 3))
print("Reshaped array_1 to 2x3:\n", reshaped_array_1)


zero_array = np.zeros((2, 3))
print("Zero array:\n", zero_array)

# random function to generate random numbers
random_array = np.random.rand(2, 3)
print("Random array:\n", random_array)