from prophet import Prophet
import pandas as pd

# Load the pre-processed dataset
grouped_data = pd.read_csv('grouped_sales_data.csv', parse_dates=['ds'])

# Create an empty list to store the forecasts
all_forecasts = []

# Get unique cities and products
unique_cities = grouped_data['City'].unique()
unique_products = grouped_data['Product'].unique()

# Loop through each city and product
for city in unique_cities:
    for product in unique_products:
        # Filter the data for the current city and product
        filtered_data = grouped_data[(grouped_data['City'] == city) & (grouped_data['Product'] == product)]

        # Check if there is sufficient data for the current city-product combination
        if filtered_data.shape[0] < 2:
            print(f"Skipping {product} in {city} due to insufficient data.")
            continue

        print(f"Training Prophet model for {product} in {city}...")

        # Initialize the Prophet model
        model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
        model.fit(filtered_data)

        # Create a future dataframe (e.g., forecast next 90 days)
        future = model.make_future_dataframe(periods=90)

        # Generate the forecast
        forecast = model.predict(future)

        # Add 'Product' and 'City' columns to the forecast DataFrame
        forecast['Product'] = product
        forecast['City'] = city

        # Append the forecast to the list
        all_forecasts.append(forecast[['ds', 'Product', 'City', 'yhat', 'yhat_lower', 'yhat_upper']])

# Concatenate all forecasts into a single DataFrame
final_forecast = pd.concat(all_forecasts, ignore_index=True)

# Save the final forecast summary to a CSV file
final_forecast.to_csv('summary_forecast.csv', index=False)

print("Summary forecast saved as 'summary_forecast.csv'.")
