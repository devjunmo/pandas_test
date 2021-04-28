import pandas as pd

df1 = pd.DataFrame({'A': ['A1', 'A2', 'A3'],
                    'B': ['B1', 'B2', 'B3'],
                    'C': ['C1', 'C2', 'C3']},
                   index=['ONE', 'TWO', 'THREE'])
print(df1)
#         A   B   C
# ONE    A1  B1  C1
# TWO    A2  B2  C2
# THREE  A3  B3  C3

df2 = pd.DataFrame({'C': ['C2', 'C3', 'C4'],
                    'D': ['D2', 'D3', 'D4']},
                   index=['TWO', 'THREE', 'FOUR'])
print(df2)
#         C   D
# TWO    C2  D2
# THREE  C3  D3
# FOUR   C4  D4

s1 = pd.Series(['X1', 'X2', 'X3'], index=['ONE', 'TWO', 'THREE'], name='X')
print(s1)
# ONE      X1
# TWO      X2
# THREE    X3
# Name: X, dtype: object

s2 = pd.Series(['Y2', 'Y3', 'Y4'], index=['TWO', 'THREE', 'FOUR'], name='Y')
print(s2)
# TWO      Y2
# THREE    Y3
# FOUR     Y4
# Name: Y, dtype: object


df_concat = pd.concat([df1, df2, df1]) # 단순 가져다 붙이기. call by value
print(df_concat)
"""         A    B   C    D
ONE     A1   B1  C1  NaN
TWO     A2   B2  C2  NaN
THREE   A3   B3  C3  NaN
TWO    NaN  NaN  C2   D2
THREE  NaN  NaN  C3   D3
FOUR   NaN  NaN  C4   D4
ONE     A1   B1  C1  NaN
TWO     A2   B2  C2  NaN
THREE   A3   B3  C3  NaN"""

df_v = pd.concat([df1, df2], axis=0)# 디폴트 = 아래에 가져다 붙임. (세로방향)
print(df_v)
df_h = pd.concat([df1, df2], axis=1)# 옆에다 갖다 붙임. 가로방향.
print(df_h)


# Series의 경우 세로로 붙이면 자료형이 유지되지만, 가로로 붙이면 데이터 프레임 형이 된다.
s1 = pd.Series(['X1', 'X2', 'X3'], index=['ONE', 'TWO', 'THREE'], name='X')
s2 = pd.Series(['Y2', 'Y3', 'Y4'], index=['TWO', 'THREE', 'FOUR'], name='Y')

s_v = pd.concat([s1, s2])
print(s_v)
print(type(s_v))
s_h = pd.concat([s1, s2], axis=1)
print(s_h)
print(type(s_h))

# 데이터 프레임 구조에 시리즈를 concat으로 추가할수도 있다.

df_s_v = pd.concat([df1, s2])
print(df_s_v) # 세로방향 concat은 index중복 상관 없이 그냥 붙인다.

df_s_h = pd.concat([df1, s2], axis=1)
print(df_s_h) # 가로방향 concat은 중복된 인덱스가 있으면 겹쳐져서 붙는다. 당연함.






















































