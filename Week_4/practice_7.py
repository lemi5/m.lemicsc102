import pandas as pd


data = {'Name': ['Clem', 'Prince', 'Edward', 'Adele'],
        'Age': [27, 24, 22, 32],
        'Address': ['Abuja', 'Kano', 'Minna', 'Lagos']}
df = pd.DataFrame(data)
df.to_csv("data11.csv")