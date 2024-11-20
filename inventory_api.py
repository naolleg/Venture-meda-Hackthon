from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

# Paths to your CSV files
inventory_csv = 'current_inventory.csv'
forecast_csv = 'summary_forecast.csv'

@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory Management API!"}

@app.get("/restock_monthly")
def restock_monthly():
    """
    Endpoint to calculate monthly restock orders.
    """
    try:
        # Load your current inventory data
        inventory_df = pd.read_csv(inventory_csv)
        forecast_df = pd.read_csv(forecast_csv)

        # Merge inventory data with forecast data
        merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

        # Adjust the forecast for monthly demand
        merged_df['Monthly_Forecast'] = merged_df['yhat'] * 4  # Adjust to monthly forecast

        # Calculate reorder points
        merged_df['Reorder_Point'] = merged_df['Monthly_Forecast'] * 1.1  # Add 10% buffer

        # Identify products that need restocking
        restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]
        restock_df = restock_df.drop_duplicates(subset=['Product', 'City'])

        # Calculate how much to order
        restock_df['Order_Quantity'] = (restock_df['Reorder_Point'] - restock_df['Stock_Level']).clip(lower=0).round()

        # Prepare JSON response
        restock_orders = restock_df[['Product', 'City', 'Order_Quantity']].to_dict(orient='records')
        return {"restock_orders": restock_orders}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {e}")


@app.get("/restock_weekly")
def restock_weekly():
    """
    Endpoint to calculate weekly restock orders.
    """
    try:
        # Load your current inventory data
        inventory_df = pd.read_csv(inventory_csv)
        forecast_df = pd.read_csv(forecast_csv)

        # Merge inventory data with forecast data
        merged_df = inventory_df.merge(forecast_df, on=['Product', 'City'], how='left')

        # Calculate reorder points based on the weekly forecast
        merged_df['Reorder_Point'] = merged_df['yhat'] * 1.1  # 10% buffer for safety

        # Identify products that need restocking
        restock_df = merged_df[merged_df['Stock_Level'] < merged_df['Reorder_Point']]
        restock_df = restock_df.drop_duplicates(subset=['Product', 'City'])

        # Calculate how much to order
        restock_df['Order_Quantity'] = (restock_df['Reorder_Point'] - restock_df['Stock_Level']).clip(lower=0).round()

        # Prepare JSON response
        restock_orders = restock_df[['Product', 'City', 'Order_Quantity']].to_dict(orient='records')
        return {"restock_orders": restock_orders}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {e}")
