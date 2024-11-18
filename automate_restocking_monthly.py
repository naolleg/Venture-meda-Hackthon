import pandas as pd

# Load your current inventory data
inventory_df = pd.read_csv('current_inventory.csv')

# Load your forecast summary data (Assume 'yhat' contains weekly forecasts)
forecast_df = pd.read_csv('summary_forecast.csv')  # Contains 'Product', 'City', 'yhat' (weekly forecast)

# Merge inventory data with forecast data
merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

# Adjust the forecast for monthly demand by multiplying by 4 (for 4 weeks in a month)
merged_df['Monthly_Forecast'] = merged_df['yhat'] * 4  # Adjust to monthly forecast

# Calculate reorder points based on the forecast for the next month (entire monthly forecast)
merged_df['Reorder_Point'] = merged_df['Monthly_Forecast'] * 1.1  # Adding 10% buffer for safety

# Identify products that need restocking (if stock level is below reorder point)
restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]

# Ensure that we only have unique Product-City combinations by removing duplicates
restock_df = restock_df.drop_duplicates(subset=['Product', 'City'])

# Now, we will calculate how much to order for the next month for each product-city combination
def place_monthly_restock_orders(restock_df):
    for index, row in restock_df.iterrows():
        product = row['Product']
        city = row['City']
        reorder_point = row['Reorder_Point']
        stock_level = row['Stock_Level']
        
        # Calculate the order quantity for the next month
        order_quantity = reorder_point - stock_level
        
        # Only consider restock if the order quantity is positive
        if order_quantity > 0:
            order_quantity = round(order_quantity)  # Round the order quantity to the nearest integer
            
            # Print the restock order message in the required format
            print(f"Placing restock order for {product} in {city}. Order quantity: {order_quantity}")

# Call the function to calculate and place monthly restock orders
place_monthly_restock_orders(restock_df)
