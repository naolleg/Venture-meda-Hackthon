import pandas as pd
import random

# Product catalog with categories (matching the synthetic sales dataset)
product_catalog = [
    ('iPhone 14', 'Electronics'), 
    ('Samsung Galaxy S23', 'Electronics'),
    ('Sony Bravia 4K TV', 'Electronics'),
    ('LG Refrigerator', 'Home Appliances'),
    ('Nike Air Max', 'Clothing'),
    ('Adidas Ultraboost', 'Clothing'),
    ('Levi’s 501 Jeans', 'Clothing'),
    ('KitchenAid Mixer', 'Home Appliances'),
    ('Dell XPS 13 Laptop', 'Electronics'),
    ('Canon EOS R5 Camera', 'Electronics'),
    ('L’Oreal Face Cream', 'Beauty'),
    ('Maybelline Mascara', 'Beauty'),
    ('Harry Potter Box Set', 'Books'),
    ('Monopoly Board Game', 'Toys'),
    ('Wilson Tennis Racket', 'Sports'),
    ('Office Chair', 'Furniture'),
    ('Car Seat Cover', 'Automotive'),
    ('Yoga Mat', 'Sports'),
    ('Desk Organizer', 'Office Supplies'),
    ('Blender Bottle', 'Groceries'),
    ('Bose QuietComfort 35', 'Electronics'),
    ('Apple Watch Series 8', 'Electronics'),
    ('Samsung Smartwatch', 'Electronics'),
    ('Philips Hue Smart Bulbs', 'Home Appliances'),
    ('TCL Smart TV', 'Electronics'),
    ('Nike T-Shirt', 'Clothing'),
    ('Under Armour Hoodie', 'Clothing'),
    ('Levi’s Jacket', 'Clothing'),
    ('Vitamix Blender', 'Home Appliances'),
    ('Asus ROG Gaming Laptop', 'Electronics'),
    ('Seiko Watch', 'Accessories'),
    ('Smeg Coffee Machine', 'Home Appliances'),
    ('Nintendo Switch', 'Toys'),
    ('Sony PlayStation 5', 'Toys'),
    ('Fossil Watch', 'Accessories'),
    ('GoPro Hero 11', 'Electronics'),
    ('Jabra Elite 75t', 'Electronics'),
    ('Puma Running Shoes', 'Clothing'),
    ('Oculus Quest 2', 'Electronics'),
    ('Bose SoundLink Speaker', 'Electronics'),
    ('Fitbit Charge 5', 'Electronics')
]

cities = ['Addis Ababa', 'Adama', 'Hawassa', 'Bahir Dar', 'Dire Dawa', 'Jimma']
num_records = 100  # Adjust the number of records as needed

# Generate sample inventory data
inventory_data = {
    'Product': [random.choice(product_catalog)[0] for _ in range(num_records)],
    'City': [random.choice(cities) for _ in range(num_records)],
    'Stock_Level': [random.randint(10, 500) for _ in range(num_records)],  # Random stock between 10 and 500 units
    'Category': [dict(product_catalog)[product] for product in [random.choice(product_catalog)[0] for _ in range(num_records)]]
}

# Create DataFrame and save to CSV
inventory_df = pd.DataFrame(inventory_data)
inventory_df.to_csv('current_inventory.csv', index=False)

print("Sample 'current_inventory.csv' created successfully.")
