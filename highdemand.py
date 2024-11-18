import pandas as pd
import glob

# Get all forecast CSV files
forecast_files = glob.glob('forecast_*.csv')
high_demand_products = []

for file in forecast_files:
    forecast = pd.read_csv(file, parse_dates=['ds'])
    product = file.split('_')[1]
    city = file.split('_')[2].split('.')[0]
    
    # Check if the trend is upward over the last 30 days in the forecast
    if forecast['yhat'].iloc[-30:].mean() > forecast['yhat'].iloc[:30].mean():
        high_demand_products.append((product, city))

# Print high-demand products
print("High-Demand Products:")
for product, city in high_demand_products:
    print(f"Product: {product}, City: {city}")
