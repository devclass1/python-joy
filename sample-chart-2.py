# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Create sample dataset
np.random.seed(42)
dates = pd.date_range("2023-01-01", periods=90)
data = pd.DataFrame({
    "Date": dates,
    "Product_A": np.random.normal(100, 15, 90).cumsum(),
    "Product_B": np.random.normal(80, 10, 90).cumsum(),
    "Region": np.random.choice(["North", "South", "East", "West"], 90),
    "Sales_Volume": np.random.randint(50, 200, 90)
})

# Melt for categorical plots
melted_data = data.melt(id_vars=["Date", "Region"], 
                        value_vars=["Product_A", "Product_B"],
                        var_name="Product", 
                        value_name="Revenue")

# 2. Setup visualization style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 8))

# 3. Create subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Line plot (Temporal trend)
sns.lineplot(
    data=data,
    x="Date",
    y="Product_A",
    hue="Region",
    style="Region",
    markers=True,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Daily Revenue Trend by Region")
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Boxplot (Distribution)
sns.boxplot(
    data=data,
    x="Region",
    y="Sales_Volume",
    hue="Region",
    palette="Set2",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Sales Volume Distribution by Region")

# Plot 3: Bar plot (Comparison)
sns.barplot(
    data=melted_data.groupby(["Product", "Region"]).mean().reset_index(),
    x="Product",
    y="Revenue",
    hue="Region",
    ci=None,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Average Revenue by Product & Region")

# Plot 4: Scatter plot (Correlation)
sns.scatterplot(
    data=data,
    x="Product_A",
    y="Product_B",
    hue="Region",
    size="Sales_Volume",
    sizes=(20, 200),
    alpha=0.7,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Product A vs B Revenue Correlation")

# 4. Enhancements
plt.suptitle("Sales Performance Dashboard", y=1.02, fontsize=16)
plt.tight_layout()

# 5. Show plot (in Databricks use display() instead)
plt.show()

# For Databricks specifically:
# display(fig) 
# plt.close()  # Prevents duplicate displays
