import pandas as pd


data = {'Name': ['Clem', 'Prince', 'Edward', 'Adele'],
        'Age': [27, 24, 22, 32],
        'Address': ['Abuja', 'Kano', 'Minna', 'Lagos']}
df = pd.DataFrame(data)

columns = list(df)
for i in df.columns:
    print(df[i][2])
    