# Climate & Weather Analysis
# Author: Afigbo Ikechukwu Joseph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load weather dataset
url = "https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv"

df = pd.read_csv(url)

# Display basic information
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nBasic statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Convert date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Plot maximum temperature
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Max_TemperatureC"])

plt.title("Seattle Maximum Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Maximum Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
