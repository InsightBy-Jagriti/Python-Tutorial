# Pandas Advanced Concepts

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. Creating a sample DataFrame
# --------------------------------------------------

data = {
    "Name": ["Jagriti", "Alex", "Rahul", "Jagriti", "Alex"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [50000, 45000, 55000, 48000, 60000],
    "Experience": [2, 1, 3, 2, 4]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)


# --------------------------------------------------
# 2. GroupBy Operations
# --------------------------------------------------

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nTotal experience by name:")
print(df.groupby("Name")["Experience"].sum())


# --------------------------------------------------
# 3. Aggregation with Multiple Functions
# --------------------------------------------------

print("\nAggregated salary stats:")
print(df.groupby("Department")["Salary"].agg(["min", "max", "mean"]))


# --------------------------------------------------
# 4. Merge & Join
# --------------------------------------------------

dept_info = pd.DataFrame({
    "Department": ["IT", "HR"],
    "Manager": ["Amit", "Neha"]
})

merged_df = pd.merge(df, dept_info, on="Department")
print("\nMerged DataFrame:\n", merged_df)


# --------------------------------------------------
# 5. Apply Function
# --------------------------------------------------

def bonus(salary):
    return salary * 0.10

df["Bonus"] = df["Salary"].apply(bonus)
print("\nBonus column added:\n", df)


# --------------------------------------------------
# 6. Handling Missing Values
# --------------------------------------------------

df.loc[2, "Salary"] = np.nan
print("\nDataFrame with missing value:\n", df)

print("\nFilling missing salary with mean:")
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df)


# --------------------------------------------------
# 7. Sorting & Ranking
# --------------------------------------------------

print("\nSorted by Salary (descending):")
print(df.sort_values(by="Salary", ascending=False))

df["Rank"] = df["Salary"].rank(ascending=False)
print("\nSalary Rank:\n", df)


# --------------------------------------------------
# 8. Date & Time Handling
# --------------------------------------------------

df["Join_Date"] = pd.to_datetime(
    ["2023-01-10", "2022-05-15", "2021-08-20", "2023-02-01", "2020-11-11"]
)

print("\nYear of Joining:")
print(df["Join_Date"].dt.year)


print("\nPandas advanced examples completed.")

