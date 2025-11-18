import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
import os

def save_plot(fig, filename, save_dir="data/plots"):
    os.makedirs(save_dir, exist_ok=True)
    path = os.path.join(save_dir, filename)
    fig.savefig(path, bbox_inches='tight')
    print(f"Saved plot: {path}")

def plot_closing_price(df, ticker, window=50, save_fig=False, save_dir="data/plots"):
    """
    Plots the closing price with rolling average for a specific ticker.
    """
    df['MA'] = df['close'].rolling(window).mean()
    
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['date'], df['close'], label='Closing Price', color='blue')
    plt.plot(df['date'], df['MA'], label=f'{window}-day MA', color='orange')
    
    plt.title(f"{ticker} Closing Price with {window}-day MA", pad=20)
    plt.xlabel("Year")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    if save_fig:
        save_plot(fig, f"{ticker}_closing_price.png", save_dir)
    else:
        plt.show()


def plot_volume(df, ticker, window=30, save_fig=False, save_dir="data/plots"):
    """
    Plots trading volume with rolling average.
    """
    df['volume_million'] = df['volume'] / 1e6
    df['vol_ma'] = df['volume_million'].rolling(window).mean()
    
    fig, ax = plt.subplots(figsize=(12,6))
    plt.plot(df['date'], df['volume_million'], alpha=0.5, label='Daily Volume', color='skyblue')
    plt.plot(df['date'], df['vol_ma'], color='red', label=f'{window}-day MA')
    
    plt.title(f"{ticker} Trading Volume with {window}-day MA (Millions)", pad=20)
    plt.xlabel("Year")
    plt.ylabel("Volume (Millions of Shares)")
    plt.grid(True)
    plt.legend()
    
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.show()

    if save_fig:
        save_plot(fig, f"{ticker}_volume.png", save_dir)
    else:
        plt.show()


def daily_returns(df, ticker, window=20, save_fig=False, save_dir="data/plots"):
    """
    Plots daily returns with rolling average to highlight trend.
    """
    df['returns'] = df['close'].pct_change()
    df['returns_ma'] = df['returns'].rolling(window).mean()
    
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['date'], df['returns'], alpha=0.5, label='Daily Returns', color='purple')
    plt.plot(df['date'], df['returns_ma'], color='red', label=f'{window}-day MA')
    
    plt.title(f"{ticker} Daily Returns with {window}-day MA", pad=20)
    plt.xlabel("Year")
    plt.ylabel("Return")
    plt.grid(True)
    plt.legend()
    
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.show()

    if save_fig:
        save_plot(fig, f"{ticker}_daily_returns.png", save_dir)
    else:
        plt.show()


def correlation_heatmap(df, ticker, save_fig=False, save_dir="data/plots"):
    """
    Shows correlation between OHLC and volume.
    """
    corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
    fig, ax = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(f"{ticker} Feature Correlation", pad=20)
    plt.show()

    if save_fig:
        save_plot(fig, f"{ticker}_correlation.png", save_dir)
    else:
        plt.show()


if __name__ == "__main__":
    ticker="AAPL"
    df = pd.read_csv("data/stocks/AAPL.csv")
    df['date'] = pd.to_datetime(df['date'])
    
    # Closing price with rolling average
    plot_closing_price(df, ticker, window=50, save_fig=True)
    
    # Volume with rolling average
    plot_volume(df, ticker, window=30, save_fig=True)
    
    # Daily returns with rolling average
    daily_returns(df, ticker, window=20, save_fig=True)
    
    # Correlation heatmap
    correlation_heatmap(df, ticker, save_fig=True)
    
    print(f"All plots for {ticker} saved.")
