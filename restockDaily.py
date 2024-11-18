import pandas as pd

# Load your current inventory data
inventory_df = pd.read_csv('current_inventory.csv')

# Load your forecast summary data
forecast_df = pd.read_csv('summary_forecast.csv')  # Contains 'Product', 'City', 'yhat' or the correct forecast column

# Print the column names to check
print(forecast_df.columns)

# Merge inventory data with forecast data
merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

# Use the correct forecast column
merged_df['Reorder_Point'] = merged_df['yhat'] * 1.1  # Use the correct forecast column name here

# Identify products that need restocking
restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]

# Display or save products that need restocking
print("Products that need restocking:")
print(restock_df[['Product', 'City', 'Stock_Level', 'Reorder_Point']])
restock_df.to_csv('restock_needs.csv', index=False)
