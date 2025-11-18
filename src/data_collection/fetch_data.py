import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os


def download_single_stock(ticker, start_date, end_date, retries=3):
    """
    Download and format data for a single stock.
    Returns a clean DataFrame with standardized column names.
    """
    for attempt in range(retries):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)

            if not df.empty:
                df = df.reset_index()
                df["Name"] = ticker

                df = df[["Date", "Open", "High", "Low", "Close", "Volume", "Name"]]
                df.columns = ["date", "open", "high", "low", "close", "volume", "name"]

                return df

        except Exception as e:
            print(f"Attempt {attempt+1} failed for {ticker}: {e}")

    return pd.DataFrame()


def download_multiple_stocks(ticker_list, years_back=5, save_csv=False, csv_path="data/stocks_data.csv"):
    """
    Downloads data for multiple tickers and returns a combined DataFrame.
    Optionally saves the combined dataset to a CSV file.
    """
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=years_back * 365)).strftime("%Y-%m-%d")

    all_data = []
    for ticker in ticker_list:
        print(f"Downloading {ticker} ...")
        df = download_single_stock(ticker, start_date, end_date)
        if not df.empty:
            all_data.append(df)

    if not all_data:
        print("No stock data collected.")
        return pd.DataFrame()

    combined = pd.concat(all_data, ignore_index=True)

    if save_csv:
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        combined.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")

    return combined

if __name__ == "__main__":
    # Example usage
    tickers = ["AAPL", "MSFT", "GOOGL"]
    data = download_multiple_stocks(tickers, years_back=3, save_csv=False)
    print(data.head())