# Pandas Basics

import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Jagriti", "Alex", "Rahul"],
    "Age": [22, 21, 23],
    "Course": ["Python", "Data Science", "AI"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# Accessing columns
print("\nNames:")
print(df["Name"])

# Basic operations
print("\nAverage Age:", df["Age"].mean())

