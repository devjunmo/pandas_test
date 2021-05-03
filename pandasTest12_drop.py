import pandas as pd

os.system('cls')

df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']})
print(df1)

i = df1[df1["A"] == "A3"].index
i[0]
print(df1.iloc[i[0], 0])

df1.drop(i[0], inplace=True)
df1