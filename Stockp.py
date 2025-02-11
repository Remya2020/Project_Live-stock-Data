import yfinance as yf

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            print("Invalid ticker symbol or no data available.")
            return
        
        print(f"Stock: {ticker}")
        print(f"Open: {data['Open'][0]:.2f}")
        print(f"High: {data['High'][0]:.2f}")
        print(f"Low: {data['Low'][0]:.2f}")
        print(f"Close: {data['Close'][0]:.2f}")
        print(f"Volume: {data['Volume'][0]}")
    except Exception as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    ticker = input("Enter stock ticker symbol (e.g., AAPL, TSLA, MSFT): ").upper()
    get_stock_data(ticker)
