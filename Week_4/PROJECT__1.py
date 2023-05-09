#Displaying the first seven row of each dataset

import pandas as pd
data = pd.read_csv("BTC_DATA_V3.0.csv")
df = data.iloc[0:7]
print(df)
print()
data = pd.read_csv("employee_records.csv")
df = data.iloc[0:7]
print(df)
print()
data = pd.read_csv("Top-Apps-in-Google-Play.csv")
df = data.iloc[0:7]
print(df)
#Selecting the first 3 columns of ech dataset

data = pd.read_csv("BTC_DATA_V3.0.csv")
print(data[['Date', 'Price', 'Open']])
print()
data = pd.read_csv("employee_records.csv")
print(data[['Employee Names', 'Years', 'Assesment Records']])
print()
#Displaping only one row and a header of each dataset

data = pd.read_csv("BTC_DATA_V3.0.csv")
df = data.head(1)
print(df)
print()
data = pd.read_csv("employee_records.csv")
df = data.head(1)
print(df)
print()
