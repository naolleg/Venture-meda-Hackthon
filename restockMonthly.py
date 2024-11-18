import pandas as pd

# Load your current inventory data
inventory_df = pd.read_csv('current_inventory.csv')

# Load your forecast summary data
forecast_df = pd.read_csv('summary_forecast.csv')  # Contains 'Product', 'City', 'yhat' or the correct forecast column

# Print the column names to check
print(forecast_df.columns)

# Ensure 'ds' is in datetime format to extract the month
forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])

# Extract the month and year from the 'ds' column
forecast_df['Year_Month'] = forecast_df['ds'].dt.to_period('M')

# Merge inventory data with forecast data
merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

# Use the correct forecast column (e.g., 'yhat')
merged_df['Reorder_Point'] = merged_df['yhat'] * 1.1  # Adjust the reorder point by 10% for safety buffer

# Group by product, city, and year-month, and sum the reorder points
monthly_restock_df = merged_df.groupby(['Product', 'City', 'Year_Month'])['Reorder_Point'].sum().reset_index()

# Identify products that need restocking (i.e., Stock Level < Reorder Point)
restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]

# Add the 'Monthly Reorder Point' to the restock dataframe
restock_df = restock_df.merge(monthly_restock_df, on=['Product', 'City', 'Year_Month'], how='left', suffixes=('', '_Monthly'))

# Display or save products that need restocking
print("Products that need restocking:")
print(restock_df[['Product', 'City', 'Stock_Level', 'Reorder_Point_Monthly']])

# Save the monthly restock data to a CSV file
restock_df.to_csv('restock_needs_monthly.csv', index=False)
