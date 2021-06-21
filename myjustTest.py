import pandas as pd
from glob import glob

df = pd.read_csv(r'D:/clinical.csv')

print(df.head())


tmplst = ['OAS30001', 'OAS30002', 'OAS30003', 'OAS30004']

df['new'] = 0

print(df.head())

# i = df2[(df2["A"] == "A2") | (df2["B"] == "B3")].index

for tmp in tmplst:
    
    print(df[df['ID'] == tmp].index)
    i = df[df['ID'] == tmp].index
    df.loc[i, 'new'] = tmp
    print(df.head())
    # break