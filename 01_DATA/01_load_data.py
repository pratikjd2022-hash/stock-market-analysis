import pandas as pd


data = pd.read_csv("../04_stock_market_data.csv")
print(data.head())
print(data.shape)

print(data.info())
print(data.isnull().sum()) 