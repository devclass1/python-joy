import matplotlib.pyplot as plt

# Create dictionary of monthly sales data
monthly_sales = {
    'January': 125000,
    'February': 98000,
    'March': 142000,
    'April': 110500,
    'May': 156800
}

# Prepare data for plotting
months = list(monthly_sales.keys())
sales = list(monthly_sales.values())

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(months, sales, color='skyblue')

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'₹{height:,}',
             ha='center', va='bottom')

# Customize the chart
plt.title('Monthly Sales Report (INR)', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales Amount (₹)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
plt.tight_layout()
plt.show()
