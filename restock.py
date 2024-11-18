import pandas as pd

# Load your current inventory data
inventory_df = pd.read_csv('current_inventory.csv')

# Load your forecast summary data
forecast_df = pd.read_csv('forecast_summary.csv')  # Contains 'Product', 'City', 'forecast_next_30_days'

# Merge inventory data with forecast data
merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

# Calculate reorder points (e.g., forecasted next 30 days with a 10% safety buffer)
merged_df['Reorder_Point'] = merged_df['forecast_next_30_days'] * 1.1

# Identify products that need restocking
restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]

# Display or save products that need restocking
print("Products that need restocking:")
print(restock_df[['Product', 'City', 'Stock_Level', 'Reorder_Point']])
restock_df.to_csv('restock_needs.csv', index=False)
