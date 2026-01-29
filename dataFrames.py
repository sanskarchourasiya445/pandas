import pandas as pd

# Creating a DataFrame with basic operations
d = pd.DataFrame({"A": [1, 2, 3, 4], "B": [5, 6, 7, 8]})

# Mathematical operations
d["add"] = d["A"] + d["B"]
d["sub"] = d["A"] - d["B"]
d["mul"] = d["A"] * d["B"]
d["div"] = d["A"] / d["B"]
d["mod"] = d["A"] % d["B"]
d["pow"] = d["A"] ** d["B"]

# Boolean operations
d["boo"] = d["A"] < 4
d["lean"] = d["B"] >= 6

# Insert column at specific position
d.insert(2, "new", d["boo"])

print("DataFrame after all operations:")
print(d)
print()

# Deleting a column
del d["new"]
print("After deleting 'new' column:")
print(d)
print()

# Column renaming
d = d.rename(columns={"add": "addition", "sub": "subtraction"})
print("After renaming columns:")
print(d)
print()

# Dropping multiple columns
d = d.drop(columns=["mod", "pow"])
print("After dropping 'mod' and 'pow' columns:")
print(d)
print()

# Creating a new column with conditional logic
d["status"] = ["High" if x > 2 else "Low" for x in d["A"]]
print("After adding 'status' column:")
print(d)
print()

# Changing column order
d = d[["A", "B", "addition", "subtraction", "mul", "div", "boo", "lean", "status"]]
print("After reordering columns:")
print(d)
print()

# Updating column values
d["addition"] = d["addition"] * 2
print("After doubling 'addition' column:")
print(d)
print()

# Column-wise operations
d["total"] = d.sum(axis=1, numeric_only=True)
print("After adding 'total' column (sum of numeric columns):")
print(d)
