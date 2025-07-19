import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime

# ======================
# 1. SAMPLE DATA PREP
# ======================
np.random.seed(42)

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.random.randint(80, 200, 6) * 1000
expenses = sales * np.random.uniform(0.3, 0.5, 6)

# Daily trend data
date_range = pd.date_range("2023-01-01", "2023-01-31")
daily_sales = np.random.normal(5000, 1500, 31).cumsum()

# Product mix
products = ['Widget A', 'Widget B', 'Widget C']
product_sales = np.random.randint(20, 60, 3) * 1000

# ======================
# 2. CREATE DASHBOARD
# ======================
fig = make_subplots(
    rows=2, cols=2,
    specs=[
        [{"type": "bar"}, {"type": "pie"}],
        [{"type": "scatter", "colspan": 2}, None]
    ],
    subplot_titles=(
        "Monthly Sales Performance", 
        "Product Mix", 
        "Daily Sales Trend"
    )
)

# ----------------------
# Chart 1: Bar Chart (Monthly Sales)
# ----------------------
fig.add_trace(
    go.Bar(
        x=months,
        y=sales,
        name="Sales",
        marker_color='#636EFA',
        text=[f'₹{x:,.0f}' for x in sales],
        textposition='auto'
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=months,
        y=expenses,
        name="Expenses",
        marker_color='#EF553B',
        text=[f'₹{x:,.0f}' for x in expenses],
        textposition='auto'
    ),
    row=1, col=1
)

# ----------------------
# Chart 2: Pie Chart (Product Mix)
# ----------------------
fig.add_trace(
    go.Pie(
        labels=products,
        values=product_sales,
        name="Product Sales",
        marker_colors=['#00CC96', '#AB63FA', '#FFA15A'],
        hole=0.4,
        hoverinfo="label+percent+value",
        textinfo="value"
    ),
    row=1, col=2
)

# ----------------------
# Chart 3: Line Chart (Daily Trend)
# ----------------------
fig.add_trace(
    go.Scatter(
        x=date_range,
        y=daily_sales,
        mode='lines+markers',
        name="Daily Sales",
        line=dict(color='#19D3F3', width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(25, 211, 243, 0.2)'
    ),
    row=2, col=1
)

# ======================
# 3. STYLING & LAYOUT
# ======================
fig.update_layout(
    title={
        'text': f"<b>Sales Dashboard</b><br><sup>Generated on {datetime.now().strftime('%Y-%m-%d')}</sup>",
        'x':0.5,
        'font': {'size': 24}
    },
    showlegend=True,
    hovermode="x unified",
    plot_bgcolor='rgba(240,240,240,0.8)',
    paper_bgcolor='rgba(240,240,240,1)',
    height=800,
    annotations=[
        dict(
            text="All values in ₹ (INR)",
            x=0, y=1.1,
            xref="paper", yref="paper",
            showarrow=False
        )
    ]
)

# Axis formatting
fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
fig.update_yaxes(
    showgrid=True, 
    gridwidth=0.5, 
    gridcolor='lightgray',
    tickprefix="₹", 
    tickformat=",.0f"
)

# ======================
# 4. ADD INTERACTIVE CONTROLS
# ======================
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            x=1, y=1.15,
            buttons=list([
                dict(
                    label="Reset View",
                    method="relayout",
                    args=[{"xaxis.range": None, "yaxis.range": None}]
                ),
                dict(
                    label="Zoom to Q1",
                    method="relayout",
                    args=[{"xaxis.range": [0, 2]}]
                )
            ])
        )
    ]
)

# ======================
# 5. DISPLAY & SAVE
# ======================
fig.show()

# Save as HTML (uncomment to use)
# fig.write_html("sales_dashboard.html")
