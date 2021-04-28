import pandas as pd

df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]}, index=['엘리스', '밥'])
print(df)
"""     age state  point
엘리스   24    NY     64
밥     42    CA     92"""

# # 컬럼 명 출력 코드
# for col_name in df:
#     print(type(col_name))
#     print(col_name) # age, state, point 출력됨
#     print('===========\n')

print(df['age'])

for index_name, value in df['age'].iteritems():
    print(type(index_name))
    print("index명 :", index_name)
    print('~~~~~~~~')

    print(type(value))  # <class 'pandas.core.series.Series'>
    print(value)

exit(0)
# 열 단위 출력. Name값은 열이름
print("열 단위 출력")
for col_name, item in df.iteritems():
    print(type(col_name))
    print(col_name)
    print('~~~~~~~~')

    print(type(item)) # <class 'pandas.core.series.Series'>
    print(item)
    """엘리스    24
        밥      42
        Name: age, dtype: int64""" # 이런 식으로 첫열 부터 끝열 까지 착착착 나옴.
    print('---------')

    print(item['엘리스']) # 24 -> 'NY' -> 64
    print(item[0]) # 24 -> 'NY' -> 64
    print(item.엘리스) # 24 -> 'NY' -> 64
    print('=======\n')

# 행 단위 출력. Name값은 행이름
print('행단위 출력')
for index, row in df.iterrows(): # 행이 2개니까 두번 돈다
    print(type(index))
    print(index)
    print('~~~~~~~~')

    print(type(row))
    print(row)
    print('---------')

    print(row['point']) # 세번째 열에 대한 행을 추출. 즉 한 요소만 추출 64 -> 92
    print(row[2])
    print(row.point)
    print('==========\n')


# frame.Pandas형으로 가져와보기
print('frame.Pandas형으로 가져오기')

for row in df.itertuples():
    print(type(row))
    print(row) # Pandas(Index='엘리스', age=24, state='NY', point=64) 형식으로 행 출력
    print('---------')

    print(row[0]) # 64 -> 92
    print(row.point)
    print('========\n')


# 반복처리에서 특정 컬럼 값 즉시 출력
for age in df['age']:
    print(age)


# 여러 컬럼을 루프 돌리고 싶으면 zip함수 사용하기

print(df['age'])
print(zip(df['age'], df['point'])) # 출력 되지 않는다.

for age, point in zip(df['age'], df['point']):
    print(age, point)
    print(type(age), type(point)) # int형











































































