import pandas as pd
from prophet import Prophet

# Example data (replace with actual data)
data = pd.DataFrame({
    'ds': ['2024-01-01', '2024-01-02', '2024-01-03'],  # Replace with your dates
    'y': [100, 120, 110]  # Replace with your actual data (e.g., sales)
})

# Convert 'ds' to datetime
data['ds'] = pd.to_datetime(data['ds'])

# Create and fit the model
model = Prophet()
model.fit(data)

# Make a future dataframe for 30 periods (e.g., days)
future = model.make_future_dataframe(data, periods=30)  # This is the correct syntax

# Predict the future
forecast = model.predict(future)

# Extract the relevant columns for the forecast summary
forecast_summary = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# Example of adding additional columns for product and city
product_name = "Sample Product"
city_name = "Sample City"
forecast_summary['Product'] = product_name
forecast_summary['City'] = city_name

# Rename the columns as needed
forecast_summary = forecast_summary.rename(columns={'yhat': 'forecast_next_30_days'})

# Save the forecast summary to a CSV file
forecast_summary.to_csv('forecast_summary.csv', index=False)

print("Forecast summary saved as 'forecast_summary.csv'.")
