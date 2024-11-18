from prophet import Prophet
import pandas as pd

# Load the pre-processed dataset
grouped_data = pd.read_csv('grouped_sales_data.csv', parse_dates=['ds'])

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

        # Plot the forecast
        #model.plot(forecast).show()

        # Optionally, save the forecast to a CSV file
        forecast_filename = f'forecast_{product}_{city}.csv'
        forecast.to_csv(forecast_filename, index=False)
        # Save forecast to a CSV file for each product-city pair
        print(f"Forecast for {product} in {city} saved to {forecast_filename}")
