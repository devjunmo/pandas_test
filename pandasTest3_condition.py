import pandas as pd

df = pd.read_csv('pandas_sample_data.csv')
print(df)
"""      name  age state  point
0    Alice   24    NY     64
1      Bob   42    CA     92
2  Charlie   18    CA     70
3     Dave   68    TX     70
4    Ellen   24    CA     88
5    Frank   30    NY     57"""

# 마스크로 행 추출하기
mask = [True, False, True, False, True, False]
df_mask = df[mask]
print(df_mask)
"""      name  age state  point
0    Alice   24    NY     64
2  Charlie   18    CA     70
4    Ellen   24    CA     88"""

s_mask = pd.Series(mask)

print(df[-s_mask])

"""
    name  age state  point
1    Bob   42    CA     92
3   Dave   68    TX     70
5  Frank   30    NY     57
"""

# 여러 조건 사용해보기 - 단순하게 T/F로만 리턴 <- 인덱스
print(df['age'] < 35) # age열에 대해 모든행 bool값으로 리턴
print((df['state'] == 'NY')) # state열에 모든행 bool값으로 리턴
print(~(df['state'] == 'NY')) # state열에 모든행 역 bool값으로 리턴
print((df['age'] < 35) & (df['state'] == 'NY')) # 합쳐진 '하나의' 열에 모든 행 bool값으로 리턴

# 여러 조건 사용해보기 - 취득한 인덱스를 바탕으로 데이터를 출력하기
df_and = df[(df['age'] < 35) & (df['state'] == 'NY')]
print(df_and)

"""    name  age state  point
0  Alice   24    NY     64
5  Frank   30    NY     57"""






























































