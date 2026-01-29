import pandas as pd
# Creating Series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
s3 = pd.Series({'apple': 5, 'banana': 3, 'orange': 7})

print("Series examples:")
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print()

# Series attributes
print("Series attributes for s1:")
print("Values:", s1.values)
print("Index:", s1.index)
print("Dtype:", s1.dtype)
print("Shape:", s1.shape)
print()

# Series operations
print("Series operations:")
print("s1 + 10:", s1 + 10)
print("Element at index 2:", s1[2])
print()
