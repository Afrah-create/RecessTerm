
'''
# Purpose of numpy
# Numpy is a powerful library in Python that provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. It is widely used in scientific computing, data analysis, and machine learning due to its performance and ease of use.
'''
try:
	import numpy as np
except ModuleNotFoundError:
	print('numpy is not installed. Install it with: pip install numpy')
	raise SystemExit(1)

print("Numpy version:", np.__version__)


# A numpy array is a grid of values, all of the same type,
# # and is indexed by a tuple of nonnegative integers. 
# # The number of dimensions is the rank of the array;
# # the shape of an array is a tuple of integers giving the size of the array along each dimension.

# Creating a numpy array
arr = np.array([1, 2, 3, 4, 5])
#print("Numpy array:", arr)

# 2D array from a nested list
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
#print("2D Numpy array:\n", arr_2d)

# 1D array from a tuple
arr_tuple = np.array((7, 8, 9))
#print("1D Numpy array from tuple:", arr_tuple)

# 2D array from a tuple of tuples
arr_2d_tuple = np.array(((10, 11), (12, 13)))
#print("2D Numpy array from tuple of tuples:\n", arr_2d_tuple)

# Accessing elements in a numpy array
#print("First element of arr:", arr[0])
#print("Element at row 1, column 2 of arr_2d:", arr_2d[1, 2])

#print("Element at row 0, column 1 of arr_2d:", arr_2d[0, 1])


# Adding 3 to each element of the array
arr_plus_3 = arr_2d + 3
#print("Array after adding 3 to each element:", arr_plus_3)


w = np.array([[2, 5], [3, 6]])
p = np.array([[1, 2], [3, 4]])

# sum of all elements in the array
sum_w = np.sum(w)
sum_p = np.sum(p)
print("Sum of all elements in w:", sum_w)
print("Sum of all elements in p:", sum_p)

z = np.array([[1,2.3],[1.0,6.9]])

# data type of the array
print("Data type of w:", w.dtype)
print("Data type of p:", p.dtype)
print("Data type of z:", z.dtype)