import pyqtgraph as pg
from pyqtgraph.Qt import QtGui

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

# Create the application window
app = QtGui.QApplication([])
win = pg.GraphicsLayoutWidget(title="Monthly Sales Report (INR)", size=(800, 600))
win.show()

# Create the plot
plot = win.addPlot()
plot.setLabel('left', 'Sales Amount (₹)')
plot.setLabel('bottom', 'Month')
plot.showGrid(x=False, y=True, alpha=0.7)

# Create the bar graph
bg = pg.BarGraphItem(x=range(len(months)), height=sales, width=0.6, brush='skyblue')
plot.addItem(bg)

# Customize x-axis with month names
ax = plot.getAxis('bottom')
ax.setTicks([[(i, month) for i, month in enumerate(months)]])

# Add value labels on top of each bar
for i, sale in enumerate(sales):
    text = pg.TextItem(f'₹{sale:,}', anchor=(0.5, 0))
    text.setPos(i, sale)
    plot.addItem(text)

# Start Qt event loop
app.exec_()
