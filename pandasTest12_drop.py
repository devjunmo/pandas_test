import pandas as pd

# os.system('cls')

df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']})
print(df1)
"""
    A   B   C
0  A1  B1  C1
1  A2  B2  C2
2  A3  B3  C3
"""

i = df1[df1["A"] != "A2"].index
i # Int64Index([0, 2], dtype='int64') <- 인덱스 리스트 형태로 리턴됨
l_i = list(i)
l_i
i[0]
i[1]
print(df1.iloc[i[0], 0])

# df1.drop(i[0], inplace=True)
# df1
# df1
# df1.drop(i, inplace=True)
# df1 
# df1.reset_index(inplace=True, drop=True)
# df1
df1
df1.drop(l_i, inplace=True)
df1 
df1.reset_index(inplace=True, drop=True)
df1
"""
    A   B   C
1  A2  B2  C2
"""

df2 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']})
print(df2)

i = df2[(df2["A"] == "A2") | (df2["B"] == "B3")].index

print(i)

print(df2.loc[i, 'A'])


i = df2[(df2["A"] != "A3") & (df2["A"] != "A1")].index # Int64Index([1], dtype='int64')
i


i = df2[(df2["A"] != "A3") | (df2["A"] != "A1")].index # Int64Index([0, 1, 2], dtype='int64')
i