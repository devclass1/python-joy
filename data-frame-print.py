import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.random.randint(80, 200, 6) * 1000
expenses = sales * np.random.uniform(0.3, 0.5, 6)
products = ['Widget A', 'Widget B', 'Widget C']
product_sales = np.random.randint(20, 60, 3) * 1000

# Create DataFrames
monthly_df = pd.DataFrame({
    'Month': months,
    'Sales (₹)': sales,
    'Expenses (₹)': expenses
})

product_df = pd.DataFrame({
    'Product': products,
    'Sales (₹)': product_sales
})

# Print the DataFrames
print("Monthly Sales Data:")
print(monthly_df)
print("\nProduct Sales Data:")
print(product_df)

# Optional: Format the output with thousands separators
pd.options.display.float_format = '{:,.0f}'.format
print("\nFormatted Monthly Data:")
print(monthly_df)
