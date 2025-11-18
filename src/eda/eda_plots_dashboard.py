import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns

def stock_eda_dashboard(df, ticker):
    """
    Generates an EDA dashboard for a stock:
    - Trading volume with moving average
    - Closing price with moving averages (50 & 200 days)
    - Daily returns with moving average
    - Correlation heatmap
    """
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])
    
    # Prepare additional columns
    df['volume_million'] = df['volume'] / 1e6
    df['vol_ma30'] = df['volume_million'].rolling(30).mean()
    df['MA50'] = df['close'].rolling(50).mean()
    df['MA200'] = df['close'].rolling(200).mean()
    df['returns'] = df['close'].pct_change()
    df['returns_ma20'] = df['returns'].rolling(20).mean()
    
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    
    # ---------------- Volume ----------------
    axes[0, 0].plot(df['date'], df['volume_million'], alpha=0.5, label='Daily Volume')
    axes[0, 0].plot(df['date'], df['vol_ma30'], color='red', label='30-day MA')
    axes[0, 0].set_title(f"{ticker} Trading Volume (Millions)", pad=20)
    axes[0, 0].set_xlabel("Year")
    axes[0, 0].set_ylabel("Volume (M)")
    axes[0, 0].xaxis.set_major_locator(mdates.YearLocator())
    axes[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    axes[0, 0].grid(True)
    axes[0, 0].legend()
    
    # ---------------- Moving Averages ----------------
    axes[0, 1].plot(df['date'], df['close'], label='Close', color='blue')
    axes[0, 1].plot(df['date'], df['MA50'], label='50-day MA', color='orange')
    axes[0, 1].plot(df['date'], df['MA200'], label='200-day MA', color='green')
    axes[0, 1].set_title(f"{ticker} Closing price", pad=20)
    axes[0, 1].set_xlabel("Year")
    axes[0, 1].set_ylabel("Price (USD)")
    axes[0, 1].xaxis.set_major_locator(mdates.YearLocator())
    axes[0, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    axes[0, 1].grid(True)
    axes[0, 1].legend()
    
    # ---------------- Daily Returns ----------------
    axes[1, 0].plot(df['date'], df['returns'], alpha=0.5, label='Daily Returns', color='purple')
    axes[1, 0].plot(df['date'], df['returns_ma20'], color='red', label='20-day MA')
    axes[1, 0].set_title(f"{ticker} Daily Returns", pad=20)
    axes[1, 0].set_xlabel("Year")
    axes[1, 0].set_ylabel("Return")
    axes[1, 0].xaxis.set_major_locator(mdates.YearLocator())
    axes[1, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    axes[1, 0].grid(True)
    axes[1, 0].legend()
    
    # ---------------- Correlation Heatmap ----------------
    corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=axes[1, 1])
    axes[1, 1].set_title(f"{ticker} Feature Correlation", pad=20)
    
    # Increase vertical spacing between rows
    plt.subplots_adjust(hspace=0.35, wspace=0.3)
    
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/stocks/AAPL.csv")
    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])
    stock_eda_dashboard(df, "AAPL")