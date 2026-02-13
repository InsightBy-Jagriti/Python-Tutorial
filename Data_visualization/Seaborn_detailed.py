# Seaborn Detailed Tutorial

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------------------------------
# Sample Dataset
# --------------------------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [20000, 22000, 25000, 24000, 28000, 30000],
    "Profit": [4000, 4500, 5200, 5000, 6500, 7200],
    "Region": ["North", "South", "North", "West", "South", "West"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# --------------------------------------------------
# 1. Line Plot
# --------------------------------------------------

sns.lineplot(x="Month", y="Sales", data=df)
plt.title("Monthly Sales Trend")
plt.show()


# --------------------------------------------------
# 2. Bar Plot
# --------------------------------------------------

sns.barplot(x="Month", y="Profit", data=df)
plt.title("Monthly Profit")
plt.show()


# --------------------------------------------------
# 3. Scatter Plot
# --------------------------------------------------

sns.scatterplot(x="Sales", y="Profit", hue="Region", data=df)
plt.title("Sales vs Profit by Region")
plt.show()


# --------------------------------------------------
# 4. Histogram
# --------------------------------------------------

sns.histplot(df["Sales"], bins=5)
plt.title("Sales Distribution")
plt.show()


# --------------------------------------------------
# 5. Box Plot
# --------------------------------------------------

sns.boxplot(x="Region", y="Sales", data=df)
plt.title("Sales Spread by Region")
plt.show()


# --------------------------------------------------
# 6. Pair Plot (Multi-variable analysis)
# --------------------------------------------------

sns.pairplot(df[["Sales", "Profit"]])
plt.show()


# --------------------------------------------------
# 7. Heatmap (Correlation Matrix)
# --------------------------------------------------

correlation = df[["Sales", "Profit"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Correlation Matrix")
plt.show()


print("\nSeaborn detailed examples completed.")
