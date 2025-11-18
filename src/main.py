import os
import pandas as pd
from eda.eda_plots import plot_closing_price, plot_volume, daily_returns, correlation_heatmap
from data_collection_preprocessing.fetch_data import download_single_stock, clean_stock_data

def main(ticker, start_date=None, end_date=None, stocks_dir="data/stocks", save_dir="data/plots"):
    """
    Main function to fetch stock data, generate EDA plots, and save them.
    """
    
    end_date = "2025-11-01"
    start_date = "2020-11-01"
    
    # Fetch stock data
    download_single_stock(ticker, start_date, end_date, save_csv=True, base_dir=stocks_dir)

    df = pd.read_csv(os.path.join(stocks_dir, f"{ticker}.csv"))

    # Ensure 'date' is datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # ---------------- Gnerate and save plots ----------------
    
    # Closing price with rolling average
    plot_closing_price(df, ticker, window=50, save_fig=True, save_dir=save_dir)
    
    # Volume with rolling average
    plot_volume(df, ticker, window=30, save_fig=True, save_dir=save_dir)
    
    # Daily returns with rolling average
    daily_returns(df, ticker, window=20, save_fig=True, save_dir=save_dir)
    
    # Correlation heatmap
    correlation_heatmap(df, ticker, save_fig=True, save_dir=save_dir)

if __name__ == "__main__":
    ticker = "AAPL" # Change the ticker according to your assignment
    main(ticker)
