import random
import csv

# Define sample data for each field
product_names = ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard", "Mouse", "Printer", "Router", "Smartwatch", "Speaker"]
colors = ["Red", "Blue", "Green", "Black", "White", "Gray", "Yellow", "Purple", "Orange", "Pink"]

# Function to generate a random IP address
def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Function to generate the dataset
def generate_dataset(num_rows):
    dataset = []
    for _ in range(num_rows):
        product_ip = generate_ip()
        product_name = random.choice(product_names)
        color = random.choice(colors)
        quantity = random.randint(1, 100)
        dataset.append([product_ip, product_name, color, quantity])
    return dataset

# Generate 25 rows of data
data = generate_dataset(25)

# Define the file name
file_name = "product_dataset.csv"

# Write the dataset to a CSV file
with open(file_name, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Product IP", "Product Name", "Color", "Quantity"])
    # Write data rows
    writer.writerows(data)

print(f"Dataset with 25 rows has been created and saved as '{file_name}'")
