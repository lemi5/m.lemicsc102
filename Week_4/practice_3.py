import pandas as pd

data = {'Name': ['Clem', 'Prince', 'Edward', 'Adele'],
        'Age': [27, 24, 22, 32],
        'Address': ['Abuja', 'Kano', 'Minna', 'Lagos'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
df = pd.DataFrame(data)
print(df.iloc[0])
