import pandas as pd

df = pd.read_excel('Electric_Vehicle_Population_Data.xlsx')

df.info()

df['Fetched Range'].fillna(0)

df['Max Range'] = df[['Fetched Range','Electric Range']].max(axis=1)

df.to_csv('Updated_Dataset_Cleaned.csv')