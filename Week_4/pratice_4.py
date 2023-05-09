import pandas as pd
data = pd.read_csv("employee_records.csv")
print(data)
df = data.head(5)
print(df)