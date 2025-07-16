# Bar Chart Creation Code Explanation

```python
# Create a figure with specific dimensions (10 inches wide, 6 inches tall)
plt.figure(figsize=(10, 6))

# Create bar chart with:
# - x-axis values: months list
# - y-axis values: sales list
# - bar color: skyblue
# - Returns container of all bars
bars = plt.bar(months, sales, color='skyblue')

# Add value labels on top of each bar
for bar in bars:  # Loop through each bar in the chart
    height = bar.get_height()  # Get the height (value) of the current bar
    
    # Add text label at:
    # x-position: center of the bar (x + width/2)
    # y-position: top of the bar (height)
    # Text: ₹ symbol with formatted number (comma separated)
    # ha='center': horizontal alignment centered
    # va='bottom': vertical alignment at bottom of text
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'₹{height:,}',
             ha='center', va='bottom')

# Add main title to the chart:
# Text: 'Monthly Sales Report (INR)'
# fontsize: 16
# pad=20: padding of 20 points from top
plt.title('Monthly Sales Report (INR)', fontsize=16, pad=20)

# Add x-axis label:
# Text: 'Month'
# fontsize: 12
plt.xlabel('Month', fontsize=12)

# Add y-axis label:
# Text: 'Sales Amount (₹)'
# fontsize: 12
plt.ylabel('Sales Amount (₹)', fontsize=12)

# Add grid lines:
# axis='y': only horizontal grid lines
# linestyle='--': dashed lines
# alpha=0.7: 70% opacity
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate x-axis tick labels:
# rotation=45: 45 degree angle
# Helps prevent label overlapping with long text
plt.xticks(rotation=45)
