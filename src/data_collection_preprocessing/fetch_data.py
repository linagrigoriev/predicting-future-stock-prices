import yfinance as yf
import pandas as pd
# from datetime import datetime, timedelta
import os

def clean_stock_data(df):
    """
    Handles missing values and duplicates (in case they exist).
    """

    # Remove duplicates
    df = df.drop_duplicates(subset=["date"])

    # Fill missing numeric data using forward fill (common for time series)
    df = df.sort_values(by="date")
    df = df.ffill()

    df = df.reset_index(drop=True)

    return df

def download_single_stock(ticker, start_date, end_date, save_csv=False, base_dir="data/stocks", retries=3):
    """
    Download and format data for a single stock.
    Returns a clean DataFrame with standardized column names.
    """
    os.makedirs(base_dir, exist_ok=True)

    for attempt in range(retries):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)

            if not df.empty:
                df = df.reset_index()

                df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
                df.columns = ["date", "open", "high", "low", "close", "volume"]

                df = clean_stock_data(df)

                if save_csv:
                    csv_path = os.path.join(base_dir, f"{ticker}.csv")

                    # Clear existing CSV (overwrite)
                    open(csv_path, "w").close()

                    # Save new CSV
                    df.to_csv(csv_path, index=False)
                    print(f"Saved: {csv_path}")

        except Exception as e:
            print(f"Attempt {attempt+1} failed for {ticker}: {e}")

    return pd.DataFrame()


def download_multiple_stocks(ticker_list, years_back=5, save_csv=False, base_dir="data/stocks"):
    """
    Downloads data for multiple tickers and returns a combined DataFrame.
    Optionally saves the combined dataset to a CSV file.
    """
    # end_date = datetime.today().strftime("%Y-%m-%d")
    # start_date = (datetime.today() - timedelta(days=years_back * 365)).strftime("%Y-%m-%d")

    end_date = "2025-11-01"
    start_date = "2020-11-01"

    os.makedirs(base_dir, exist_ok=True)

    for ticker in ticker_list:
        print(f"Downloading {ticker} ...")
        download_single_stock(ticker, start_date, end_date, save_csv, base_dir)

if __name__ == "__main__":
    # Example usage
    tickers = ["AAPL", "MSFT", "GOOGL"]
    download_multiple_stocks(tickers, years_back=3, save_csv=True)
    # print(data.head())