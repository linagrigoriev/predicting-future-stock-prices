# Predicting Future Stock Prices

This project was developed as part of the Data Science Club at ELTE. Its aim is to analyze and forecast stock market trends using historical stock data. To achieve this, various data analysis techniques and machine learning algorithms are applied. The dataset used for the analysis is sourced from Yahoo Finance.

## Create virtual environment and activate it

### Windows (Command Prompt)
`
python -m venv venv
venv\Scripts\activate
`

### macOS / Linux
`
python3 -m venv venv
source venv/bin/activate
`

## Install packages
`pip install pandas numpy scikit-learn yfinance matplotlib seaborn`

or

`pip install -r requirements.txt`

## Stock Analysis Exercise

This exercise will help you explore a stock you were assigned to using Python. You will generate some graphs and interpret them in a simple, practical way.

**Steps for the Exercise**:

1. **Run the Main Script**
   - Make sure you have set up the virtual environment and installed the required packages.
   - Don't forget to change the ticker.
   - Run the main script:
     ```bash
     python main.py
     ```
   - The script will download the stock data, generate the graphs, and save them in the `results/plots/` folder.

2. **Look at the Graphs**
   Open the plots in `results/plots/` and answer the following questions for each one:

   ### Closing Price with Moving Average
   - How did the stock price change over time? (Did it mostly go up, down, or stay flat?)  
   - What do the moving average lines show? (Look for smooth trends vs short-term bumps.)

   ### Trading Volume with Rolling Average
   - Are there days when a lot more shares were traded than usual?  
   - Can you see periods of consistently high or low trading activity?

   ### Daily Returns with Rolling Average
   - Look for big spikes or drops. Do they happen occasionally or frequently?  
   - The moving average smooths the noise – what overall trend does it suggest?

   ### Feature Correlation Heatmap
   - Which numbers move together (e.g., Open vs Close)?  
   - Which numbers seem unrelated?  
   - orrelation values range from -1 to 1.
   
      1 → perfect positive correlation

      0 → no correlation

      -1 → perfect negative correlation

3. **Write Your Observations**
   - For each graph, write a short paragraph describing what you see.  
   - Focus on **trends, spikes, and relationships**, not exact financial calculations.

---

## Optional: Go Deeper

If you want to explore more:
- Open the scripts in the `eda/` folder.  
- Try changing the **rolling average window** (e.g., 10-day vs 50-day) and see how it changes the graphs.  
- Look at how smoothing affects what you notice in trends and spikes.  

This part is optional – the main goal is to **run the code and interpret the graphs** in simple, clear terms.