# Modules help in organizing and reusing code
import math
square = math.sqrt(16)  # Returns 4.0
pi = math.pi  # Returns 3.141592653589793

print("Square root of 16 is:", square)
print("Value of pi is:", pi)


import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
