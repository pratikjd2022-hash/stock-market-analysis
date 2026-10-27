import pandas as pd

# 1. LOAD DATA

data = pd.read_csv("../04_stock_market_data.csv")
print("DATA LOADED SUCCESSFULLY")
print("Dataset Shape:", data.shape)
print()


# 2. COMPANY-WISE CLOSING PRICE ANALYSIS

company_analysis = data.groupby("Company")["Close"].agg(
    average_close="mean",
    highest_close="max",
    lowest_close="min"
)

print("COMPANY-WISE CLOSING PRICE ANALYSIS")
print(company_analysis.round(2))
print()


# 3. COMPANY-WISE TRADING VOLUME ANALYSIS

volume_analysis = data.groupby("Company")["Volume"].agg(
    average_volume="mean",
    highest_volume="max"
)

print("COMPANY-WISE TRADING VOLUME ANALYSIS")
print(volume_analysis.round(2))
print()


# 4. DAILY RETURN CALCULATION

# Convert Date column into datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Sort data company-wise and date-wise
data = data.sort_values(["Company", "Date"]).copy()

# Get previous trading day's closing price
data["Previous_Close"] = (
    data.groupby("Company")["Close"].shift(1)
)

# Calculate daily percentage return
data["Daily_Return_Pct"] = (
    (data["Close"] - data["Previous_Close"])
    / data["Previous_Close"] * 100
)

print("DAILY RETURN SAMPLE")
print(
    data[
        ["Company", "Date", "Close", "Daily_Return_Pct"]
    ].head(10).round(2)
)
print()


# 5. DAILY RETURN ANALYSIS

return_analysis = data.groupby("Company")["Daily_Return_Pct"].agg(
    average_daily_return="mean",
    best_daily_return="max",
    worst_daily_return="min"
)

print("COMPANY-WISE DAILY RETURN ANALYSIS")
print(return_analysis.round(2))
print()


# 6. MONTHLY AVERAGE CLOSING PRICE ANALYSIS

data["Month"] = data["Date"].dt.to_period("M")

monthly_analysis = data.groupby(
    ["Company", "Month"]
)["Close"].mean().round(2)

print("MONTHLY AVERAGE CLOSING PRICE ANALYSIS")
print(monthly_analysis)
print()


# 7. COMPANY-WISE OVERALL SUMMARY

overall_summary = data.groupby("Company").agg(
    total_records=("Close", "count"),
    average_close=("Close", "mean"),
    highest_close=("Close", "max"),
    lowest_close=("Close", "min"),
    average_volume=("Volume", "mean"),
    average_daily_return=("Daily_Return_Pct", "mean")
)

print("FINAL COMPANY-WISE SUMMARY")
print(overall_summary.round(2))
print()


# 8. SAVE ANALYSIS DATA

data.to_csv("../05_stock_market_analysis_results.csv", index=False)
print("Analysis completed successfully!")
print("Results saved to stock_market_analysis_results.csv")

# Step	        Analysis	                  Kya pata chalega?
# 1	            Load data	                Dataset load hua ya nahi
# 2	            Closing price	            Average, highest aur lowest close
# 3	            Volume                 	    Average aur maximum trading volume
# 4	            Daily return	            Har trading day ka percentage change
# 5	            Return analysis	            Average, best aur worst daily return
# 6	            Monthly analysis	        Har month ka average closing price
# 7	            Overall summary	            Sabhi important metrics ka combined summary
# 8	            Save results	            Analysis columns wali CSV file save hogi