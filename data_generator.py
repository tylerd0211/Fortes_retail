import pandas as pd
import random
from datetime import datetime, timedelta

# Define columns
columns = [
    "OrderID", "CustomerID", "OrderDate", "ShipDate", "OrderAmount", "OrderStatus", "PaymentMethod", "ShippingAddress", "ProductID", "Quantity"
]

# Helper functions
def random_date(start, end):
    """Generate a random datetime between two dates."""
    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_random_address():
    streets = ["Main St", "Elm St", "Maple Ave", "Oak Dr", "Pine Rd"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    return f"{random.randint(100, 999)} {random.choice(streets)}, {random.choice(cities)}"

# Define constants
start_years = [2023, 2024, 2025]
months = [1, 2, 3]  # Jan to March
statuses = ["Pending", "Shipped", "Delivered", "Cancelled"]
payment_methods = ["Credit Card", "PayPal", "Bank Transfer"]

# Generate data
rows = []
for i in range(1, 21):
    order_year = random.choice(start_years)
    order_month = random.choice(months)
    order_date = datetime(order_year, order_month, random.randint(1, 28))
    ship_date = order_date + timedelta(days=random.randint(1, 10))
    row = [
        i,  # OrderID
        random.randint(1, 100),  # CustomerID
        order_date,  # OrderDate
        ship_date,  # ShipDate
        round(random.uniform(10, 1000), 2),  # OrderAmount
        random.choice(statuses),  # OrderStatus
        random.choice(payment_methods),  # PaymentMethod
        generate_random_address(),  # ShippingAddress
        random.randint(1, 50),  # ProductID
        random.randint(1, 10)  # Quantity
    ]
    rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows, columns=columns)

# Save to CSV
csv_file_path = "/Users/ravitejanb/Documents/Fortes_retail/orders_table.csv"
df.to_csv(csv_file_path, index=False)


