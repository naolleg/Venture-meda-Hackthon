import pandas as pd

# Load your current inventory data
inventory_df = pd.read_csv('current_inventory.csv')

# Load your forecast summary data
forecast_df = pd.read_csv('summary_forecast.csv')  # Contains 'Product', 'City', 'yhat' or the correct forecast column

# Print the column names to check
print(forecast_df.columns)

# Ensure 'ds' is in datetime format to extract week
forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])

# Extract the week number
forecast_df['Week'] = forecast_df['ds'].dt.isocalendar().week

# Merge inventory data with forecast data
merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

# Use the correct forecast column (e.g., 'yhat')
merged_df['Reorder_Point'] = merged_df['yhat'] * 1.1  # Adjust the reorder point by 10% for safety buffer

# Group by product, city, and week, and sum the reorder points
weekly_restock_df = merged_df.groupby(['Product', 'City', 'Week'])['Reorder_Point'].sum().reset_index()

# Identify products that need restocking (i.e., Stock Level < Reorder Point)
restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]

# Add the 'Weekly Reorder Point' to the restock dataframe
restock_df = restock_df.merge(weekly_restock_df, on=['Product', 'City', 'Week'], how='left', suffixes=('', '_Weekly'))

# Display or save products that need restocking
print("Products that need restocking:")
print(restock_df[['Product', 'City', 'Stock_Level', 'Reorder_Point_Weekly']])

# Save the weekly restock data to a CSV file
restock_df.to_csv('restock_needs_weekly.csv', index=False)
