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

df_i = df.set_index('name') # call by value. 주key 느낌의 컬럼을 인덱스의 이름으로 갖다 박음. 해당 열은 drop.
print(df_i)
"""         age state  point
name                     
Alice     24    NY     64
Bob       42    CA     24
Charlie   18    CA     70
Dave      68    TX     70
Ellen     24    CA     88
Frank     30    NY     57"""

print(df.set_index('name', drop=False)) # 사용한 열 drop 방지.

df_i_multi = df.set_index(['state', 'name'])
print(df_i_multi)
"""               age  point
state name               
NY    Alice     24     64
CA    Bob       42     24
      Charlie   18     70
TX    Dave      68     70
CA    Ellen     24     88
NY    Frank     30     57 # 중복된 컬럼은 생략되는게 제맛임. CA나 NY 중복 남아있으니, sort 해서 제대로 생략되도록!
"""

df_m = df.set_index(['state', 'name'])
print(df_m.sort_index(inplace=False)) # 맨 왼쪽 인덱스 네임 기준 소팅임.
"""
state name               
CA    Bob       42     24
      Charlie   18     70
      Ellen     24     88
NY    Alice     24     64
      Frank     30     57
TX    Dave      68     70"""


df_m = df.set_index(['name', 'state'])
print(df_m.sort_index(inplace=False))
"""               age  point
name    state            
Alice   NY      24     64
Bob     CA      42     24
Charlie CA      18     70
Dave    TX      68     70
Ellen   CA      24     88
Frank   NY      30     57"""

# 인덱스 '추가'하기 -> append
df_i = df.set_index('name')
print(df_i)
df_ii = df_i.set_index('state') # 기존의 index에 덮어쓰기됨. 데이터 손실
print(df_ii)

df_mi = df_i.set_index('state', append=True)
print(df_mi)
"""               age  point
name    state            
Alice   NY      24     64
Bob     CA      42     24
Charlie CA      18     70
Dave    TX      68     70
Ellen   CA      24     88
Frank   NY      30     57
""" # append ok

print(df_mi.swaplevel(0, 1)) # call by value

print(df_mi.reset_index()) # 인덱스 초기화 및 컬럼 복구

# loc()과 at()을 통해 지정한 인덱스 사용하여 값 뽑기

print(df_mi)
print(df_mi.loc['Bob'])
"""
       age  point
state            
CA      42     24
"""
print(df)
df.set_index('name', inplace=True)
print(df)
# print(df_mi.at['Bob', 'age']) # 알수없는 오류
# print(df_mi.reset_index().set_index('name').at['Bob', 'age'])


























































