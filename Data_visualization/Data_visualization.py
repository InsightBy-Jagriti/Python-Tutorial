# Data Visualization using Matplotlib & Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# --------------------------------------------------
# Sample Data
# --------------------------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [200, 250, 300, 280, 350],
    "Profit": [50, 70, 90, 85, 120]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 1. Line Plot (Matplotlib)
# --------------------------------------------------

plt.figure()
plt.plot(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()


# --------------------------------------------------
# 2. Bar Chart (Matplotlib)
# --------------------------------------------------

plt.figure()
plt.bar(df["Month"], df["Profit"])
plt.xlabel("Month")
plt.ylabel("Profit")
plt.title("Monthly Profit")
plt.show()


# --------------------------------------------------
# 3. Scatter Plot (Matplotlib)
# --------------------------------------------------

plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()


# --------------------------------------------------
# 4. Histogram (Seaborn)
# --------------------------------------------------

sns.histplot(df["Sales"])
plt.title("Sales Distribution")
plt.show()


# --------------------------------------------------
# 5. Box Plot (Seaborn)
# --------------------------------------------------

sns.boxplot(data=df[["Sales", "Profit"]])
plt.title("Sales & Profit Spread")
plt.show()


print("Data visualization examples completed.")
