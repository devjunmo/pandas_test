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

print(df.replace('CA', 'Calif')) # call by value
print(df.replace(24, 100))

# call by value
new_df = df.replace('CA', 'Calif')
print(new_df)

# call by reference
df.replace('CA', 'Calif', inplace=True)
print(df)

df.replace('al', 'mmm', inplace=True) # 국소 치환은 안됨.
print(df)


# 여러 문자열 치환하기 -> 딕셔너리 폼 또는 리스트폼으로..

print(df.replace({'NY':'NewYork', 'TX':'TXXX'}))
print(df.replace(['NY', 'TX'], ['NewYork', 'TXXX'])) # [바꿀리스트], [결과값 리스트] or 단일 값


# 특정 컬럼의 특정 값만 지정하여 값 치환하기
print(df.replace({'age':{24:100}}))

# 여러 컬럼의 특정 값들에 대해 하나의 값으로 치환하기
print(df.replace({'age': 24, 'point': 70}, 1000))




































































