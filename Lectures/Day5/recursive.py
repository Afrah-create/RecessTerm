# recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))



def count_down(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        count_down(n - 1)
count_down(5)

# first 10 numbers in the Fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

for i in range(10):
    print(fibonacci(i))



# binary search using recursion
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
