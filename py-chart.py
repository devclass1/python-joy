import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data
monthly_sales = {
    'January': 125000,
    'February': 98000,
    'March': 142000,
    'April': 110500,
    'May': 156800
}

# Create figure
fig = go.Figure()

# Add bar trace
fig.add_trace(go.Bar(
    x=list(monthly_sales.keys()),
    y=list(monthly_sales.values()),
    text=[f'₹{x:,.0f}' for x in monthly_sales.values()],
    textposition='outside',
    marker_color='#1f77b4',
    hoverinfo='y+text',
    hovertemplate='<b>%{x}</b><br>Sales: ₹%{y:,.0f}<extra></extra>',
    name='Monthly Sales'
))

# Styling
fig.update_layout(
    title={
        'text': "<b>Monthly Sales Report (INR)</b>",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 24}
    },
    xaxis={
        'title': '<b>Month</b>',
        'tickangle': -45,
        'gridcolor': 'lightgray'
    },
    yaxis={
        'title': '<b>Sales Amount (₹)</b>',
        'gridcolor': 'lightgray',
        'zeroline': False
    },
    plot_bgcolor='white',
    hoverlabel={
        'bgcolor': 'white',
        'font_size': 14
    },
    margin={'l': 80, 'r': 80, 't': 100, 'b': 80},
    height=600,
    width=900
)

# Add horizontal grid lines
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')

# Add average line
avg_sales = sum(monthly_sales.values())/len(monthly_sales)
fig.add_shape(
    type="line",
    x0=-0.5,
    y0=avg_sales,
    x1=len(monthly_sales)-0.5,
    y1=avg_sales,
    line=dict(color="red", width=2, dash="dash"),
    name="Average"
)

# Add annotation for average
fig.add_annotation(
    x=len(monthly_sales)-1,
    y=avg_sales,
    text=f"Average: ₹{avg_sales:,.0f}",
    showarrow=True,
    arrowhead=1,
    ax=0,
    ay=-40,
    bgcolor="white",
    bordercolor="red"
)

# Show figure
fig.show()

# To save as HTML:
# fig.write_html("monthly_sales.html")
