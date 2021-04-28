import pandas as pd

df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie']
                      , 'age': [24, 42, 35]
                      , 'state': ['NY', 'CA', 'LA']
                      , 'point': [64, 92, 75]})
print(df)
"""      name  age state  point
0    Alice   24    NY     64
1      Bob   42    CA     92
2  Charlie   35    LA     75"""

# 특정 열에 해당하는 값들에 대해 내가 원하는 문자열 결합하기
print(df['name'].str.cat(['결합', '하려는', '리스트'], sep=' -_- '))
# print(df['name'].str.cat(df['age'], sep='')) # 불가

# 플러스 연산자로 문자열 결합하기
print(df['name'] + ' in ' + df['state'])
df['뉴컬럼'] = df['name'] + ' in ' + df['state']
print(df)

print(df['name'] + ' 하 ' + df['state'] + ' - ' + ["가", "나", "다"])

# 문자열과 숫자 합치기
print(df['name'].str.cat(map(str, [10, 20, 30]), sep='-'))















































