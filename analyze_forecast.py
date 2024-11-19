import pandas as pd
import glob
import matplotlib.pyplot as plt

# Get all forecast CSV files
forecast_files = glob.glob('forecast_*.csv')

# Loop through each file and plot the forecast
for file in forecast_files:
    forecast = pd.read_csv(file, parse_dates=['ds'])
    
    # Plot the forecast trend
    plt.figure(figsize=(10, 5))
    plt.plot(forecast['ds'], forecast['yhat'], label='Forecast')
    plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='lightgrey', label='Confidence Interval')
    plt.title(f"Forecast Analysis for {file.split('_')[1]} in {file.split('_')[2].split('.')[0]}")
    plt.xlabel('Date')
    plt.ylabel('Predicted Sales')
    plt.legend()
    plt.tight_layout()  # Adjusts the plot to fit within the figure area

# Show all plots after the loop completes
plt.show()
