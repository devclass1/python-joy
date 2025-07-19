import plotly.express as px

monthly_sales = {
    'January': 125000,
    'February': 98000,
    'March': 142000,
    'April': 110500,
    'May': 156800
}

fig = px.bar(
    x=list(monthly_sales.keys()),
    y=list(monthly_sales.values()),
    text=[f'₹{x:,}' for x in monthly_sales.values()],
    labels={'x': 'Month', 'y': 'Sales Amount (₹)'},
    title='Monthly Sales Report (INR)'
)

fig.update_traces(
    marker_color='skyblue',
    textposition='outside'
)

fig.update_layout(
    yaxis_gridcolor='lightgray',
    yaxis_gridwidth=0.5,
    yaxis_zeroline=False
)

fig.show()
