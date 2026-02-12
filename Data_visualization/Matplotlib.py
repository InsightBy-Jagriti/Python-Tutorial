# Matplotlib Detailed Tutorial
# ----------------------------
# This file covers the most commonly used plots in Matplotlib
# with clear structure and real-world style examples.

import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
# Sample Dataset (created using Pandas)
# --------------------------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20000, 22000, 25000, 24000, 28000, 30000],
    "Profit": [4000, 4500, 5200, 5000, 6500, 7200]
}

df = pd.DataFrame(data)

print("Dataset Used:")
print(df)


# --------------------------------------------------
# 1. Line Plot (Trend Analysis)
# --------------------------------------------------
# Used to show trends over time

plt.figure()
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()


# --------------------------------------------------
# 2. Bar Chart (Comparison)
# --------------------------------------------------
# Used to compare values across categories

plt.figure()
plt.bar(df["Month"], df["Profit"])
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit Comparison")
plt.show()


# --------------------------------------------------
# 3. Scatter Plot (Relationship Between Variables)
# --------------------------------------------------
# Used to find relationships or patterns

plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit Relationship")
plt.show()


# --------------------------------------------------
# 4. Histogram (Distribution)
# --------------------------------------------------
# Used to understand frequency distribution

plt.figure()
plt.hist(df["Sales"], bins=5)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")
plt.show()


# --------------------------------------------------
# 5. Pie Chart (Proportion)
# --------------------------------------------------
# Used to show contribution of parts to whole

plt.figure()
plt.pie(
    df["Profit"],
    labels=df["Month"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Profit Contribution by Month")
plt.show()


# --------------------------------------------------
# 6. Multiple Lines in One Plot
# --------------------------------------------------
# Used to compare trends together

plt.figure()
plt.plot(df["Month"], df["Sales"], label="Sales")
plt.plot(df["Month"], df["Profit"], label="Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.title("Sales vs Profit Trend")
plt.legend()
plt.show()


# --------------------------------------------------
# 7. Customizing Plots
# --------------------------------------------------
# Adding grid, markers, and styling

plt.figure()
plt.plot(df["Month"], df["Sales"], marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Styled Sales Plot")
plt.grid(True)
plt.show()


# --------------------------------------------------
# 8. Saving a Plot
# --------------------------------------------------
# Useful for reports and dashboards

plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Sales Chart Saved")
plt.savefig("sales_chart.png")
plt.close()

print("\nMatplotlib detailed examples completed.")

