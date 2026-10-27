import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("../03_CHARTS", exist_ok=True)

# 1. LOAD DATA

data = pd.read_csv("../04_stock_market_data.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values(["Company", "Date"]).copy()

print("DATA LOADED SUCCESSFULLY")
print("Dataset Shape:", data.shape)


# 2. COMPANY-WISE AVERAGE CLOSING PRICE

company_prices = data.groupby("Company")["Close"].mean()

plt.figure(figsize=(10, 6))
company_prices.plot(kind="bar")

plt.title("Company-wise Average Closing Price")
plt.xlabel("Company")
plt.ylabel("Average Closing Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/average_closing_price.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 3. COMPANY-WISE HIGHEST AND LOWEST PRICE

price_comparison = data.groupby("Company")["Close"].agg(
    Highest="max",
    Lowest="min"
)

price_comparison.plot(kind="bar", figsize=(10, 6))

plt.title("Highest vs Lowest Closing Price")
plt.xlabel("Company")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/highest_vs_lowest_price.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 4. STOCK CLOSING PRICE TREND

plt.figure(figsize=(12, 6))

for company in data["Company"].unique():
    company_data = data[data["Company"] == company]

    plt.plot(
        company_data["Date"],
        company_data["Close"],
        label=company
    )

plt.title("Stock Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/closing_price_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 5. MONTHLY AVERAGE CLOSING PRICE

data["Month"] = data["Date"].dt.to_period("M")

monthly_prices = data.groupby(
    ["Month", "Company"]
)["Close"].mean().unstack()

monthly_prices.plot(figsize=(12, 6), marker="o")

plt.title("Monthly Average Closing Price")
plt.xlabel("Month")
plt.ylabel("Average Closing Price")
plt.legend(title="Company")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/monthly_average_price.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 6. COMPANY-WISE AVERAGE TRADING VOLUME

average_volume = data.groupby("Company")["Volume"].mean()

plt.figure(figsize=(10, 6))
average_volume.plot(kind="bar")

plt.title("Company-wise Average Trading Volume")
plt.xlabel("Company")
plt.ylabel("Average Trading Volume")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 7. DAILY RETURN DISTRIBUTION

data["Previous_Close"] = (
    data.groupby("Company")["Close"].shift(1)
)

data["Daily_Return_Pct"] = (
    (data["Close"] - data["Previous_Close"])
    / data["Previous_Close"] * 100
)

plt.figure(figsize=(10, 6))

sns.histplot(
    data=data,
    x="Daily_Return_Pct",
    bins=40,
    kde=True
)

plt.title("Distribution of Daily Stock Returns")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(
    "charts/average_trading_volume.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 8. COMPANY-WISE DAILY RETURN COMPARISON

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=data,
    x="Company",
    y="Daily_Return_Pct"
)

plt.title("Daily Return Distribution by Company")
plt.xlabel("Company")
plt.ylabel("Daily Return (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "charts/daily_return_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 9. OPEN PRICE VS CLOSE PRICE

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=data,
    x="Open",
    y="Close",
    hue="Company"
)

plt.title("Opening Price vs Closing Price")
plt.xlabel("Opening Price")
plt.ylabel("Closing Price")
plt.tight_layout()
plt.savefig(
    "charts/daily_return_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 10. STOCK DATA CORRELATION HEATMAP

numeric_data = data[
    ["Open", "High", "Low", "Close", "Volume"]
]

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Stock Market Data Correlation Heatmap")
plt.tight_layout()
plt.savefig(
    "charts/open_vs_close_scatterplot.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 11. SAVE CHART DATA

data.to_csv("../06_stock_market_visualization_data.csv", index=False)
print("All visualizations completed successfully!")
print("Visualization data saved successfully.")    

