# Sales Data Analysis using CSV and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Read CSV file
# --------------------------------------------------

df = pd.read_csv("sales_data.csv")

print("Sales Data:")
print(df)


# --------------------------------------------------
# 2. Basic Analysis
# --------------------------------------------------

print("\nTotal Sales:", df["Sales"].sum())
print("Average Profit:", df["Profit"].mean())


# --------------------------------------------------
# 3. Line Plot: Monthly Sales Trend
# --------------------------------------------------

plt.figure()
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()


# --------------------------------------------------
# 4. Bar Chart: Monthly Profit
# --------------------------------------------------

plt.figure()
plt.bar(df["Month"], df["Profit"])
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit Analysis")
plt.show()


print("Sales analysis completed successfully.")

