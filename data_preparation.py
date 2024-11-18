import pandas as pd

# Step 1: Load your synthetic sales data
df = pd.read_csv('synthetic_sales_data.csv', parse_dates=['SalesTime'])

# Step 2: Convert 'SalesTime' to just date (if necessary)
df['SalesDate'] = df['SalesTime'].dt.date

# Step 3: Group the data by city, product, and date (sum the sales amount)
grouped_data = df.groupby(['City', 'Product', 'SalesDate']).agg({'Amount': 'sum'}).reset_index()

# Step 4: Rename columns to match Prophet's format
grouped_data.rename(columns={'SalesDate': 'ds', 'Amount': 'y'}, inplace=True)

# Check the first few rows of the data to confirm it's in the correct format
print(grouped_data.head())

# Save the grouped data to a CSV file
grouped_data.to_csv('grouped_sales_data.csv', index=False)
print("Grouped data saved as 'grouped_sales_data.csv'")
