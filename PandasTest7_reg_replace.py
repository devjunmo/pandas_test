import pandas as pd

df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Dave','Ellen','Frank'],
                   'age': [24,42,18,68,24,30],
                   'state': ['NY','CA','CA','TX','CA','NY'],
                   'point': [64,24,70,70,88,57]}
                  )
print(df)
"""      name  age state  point
0    Alice   24    NY     64
1      Bob   42    CA     24
2  Charlie   18    CA     70
3     Dave   68    TX     70
4    Ellen   24    CA     88
5    Frank   30    NY     57"""

print(df.replace('()li()', r'\1LI\2', regex=True))


# 특정 컬럼에 대해 국소 replace 할때 정규표현식 안써도 가능
df['name'] = df['name'].str.replace('li', 'LI')
print(df)
