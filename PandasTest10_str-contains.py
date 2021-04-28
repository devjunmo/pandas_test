import pandas as pd

df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Dave','Ellen','Frank'],
                   'age': [24,42,18,68,24,30],
                   'state': ['NY','CA','CA','TX','CA','NY'],
                   'point': [64,24,70,70,88,57]}
                  )

print(df)

print(df['name'].str.contains('li')) # 부분 일치 하는것을 찾는다.
"""
0     True
1    False
2     True
3    False
4    False
5    False
Name: name, dtype: bool"""

print(df[df['name'].str.contains('li')])
"""      name  age state  point
0    Alice   24    NY     64
2  Charlie   18    CA     70
"""











































































