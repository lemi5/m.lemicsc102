import pandas as pd
#data = pd.read_csv("employee_records.csv")
#df = data.iloc[0]

#print(df)

data = {'Name': ['Clem', 'Prince', 'Edward', 'Adele'],
        'Age': [27, 24, 22, 32],
        'Address': ['Abuja', 'Kano', 'Minna', 'Lagos']}
df = pd.DataFrame(data)
for i, j in df.iterrows():
    print(i, j)
    print()