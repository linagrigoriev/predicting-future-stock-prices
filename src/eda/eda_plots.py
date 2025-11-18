import matplotlib.pyplot as plt


def plot_closing_price(df, ticker):
    """
    Plots the closing price for a specific ticker.
    """

    stock_df = df[df["name"] == ticker]

    plt.figure(figsize=(10, 6))
    plt.plot(stock_df["date"], stock_df["close"], label="Closing Price")
    plt.title(f"{ticker} Stock Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid()
    plt.legend()
    plt.show()
