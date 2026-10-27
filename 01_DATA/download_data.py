
import yfinance as yf
import pandas as pd

stocks = {
    "RELIANCE.NS": "Reliance",
    "TCS.NS": "TCS",
    "INFY.NS": "Infosys",
    "HDFCBANK.NS": "HDFC_Bank",
    "ICICIBANK.NS": "ICICI_Bank"
}

all_data = []

for ticker, company in stocks.items():
    print(f"Downloading {company}...")

    df = yf.download(
        ticker,
        period="1y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    if df.empty:
        print(f"Data not available: {company}")
        continue

    df = df.reset_index()

    df.columns = [
        col[0] if isinstance(col, tuple) else col
        for col in df.columns
    ]

    df["Company"] = company
    all_data.append(df)

if all_data:
    final_data = pd.concat(all_data, ignore_index=True)

    final_data.to_csv("../04_stock_market_data.csv", index=False)

    print("\nFirst 5 rows:")
    print(final_data.head())

    print("\nDataset shape:")
    print(final_data.shape)

    print("\nCompany-wise row counts:")
    print(final_data["Company"].value_counts())

    print("\nMissing values:")
    print(final_data.isnull().sum())

    print("\nCSV saved successfully!")

else:
    print("No stock data downloaded. Please try again.")
