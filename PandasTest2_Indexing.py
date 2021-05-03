import pandas as pd
import numpy as np

ex_df = pd.DataFrame([['', 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], columns=["열1", "열2", "열3"])
print(ex_df)

###########################
# loc과 iloc은 프로퍼티임 #
###########################

def fix_missing3(df, col):
    for i in df.index:
        val = df.get_value(i, col)
        if val == 0:
            df.set_value(i, col, np.nan)

print(ex_df._set_value(0, '열1', '1'))
ex_df.at[0, '열1'] = 'th'
print('>>>', ex_df.at[0, '열1'])

# exit(0)
print(ex_df.loc[0])
"""
열1    1
열2    2
열3    3"""
# exit(0)
# print(ex_df.loc["열1"]) # 에러

print("''은 이렇게 출력된다 ->", ex_df.loc[0, "열1"])
print("''의 타입은?", type(ex_df.loc[0, "열1"]))  # <class 'str'>

print(ex_df.loc[0, "열1"] is '')

print(len(ex_df.index))

# print(ex_df.loc["열2", "행2"]) # 에러]
# exit(0)
ex_df.loc[1, "열1"] = np.nan
ex_df.loc[1, "열2"] = np.nan
ex_df.loc[1, "열3"] = np.nan
print(ex_df) # 적용됨.
ex_df.dropna(inplace=True)
print(ex_df)
ex_df.reset_index(drop=True, inplace=True)
print(ex_df)
# exit(0)

print("iloc 테스트")

print(ex_df.iloc[1])
"""
열1    4
열2    5
열3    6
Name: 행2, dtype: int64"""
ex_df

print(ex_df.iloc[1, 2])  # 6

print(ex_df.iloc[0, 0])  # 6


ex_df = pd.DataFrame([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]], columns=["열1", "열2", "열3"])
print(ex_df)

def tmp_mtd(df):
    df['new'] = np.nan
tmp_mtd(ex_df)
print(ex_df)

print(ex_df.loc[1, '열1'])
def tmp_mth2(ex_df):
    ex_df.loc[1, 'new'] = ex_df.loc[0, '열1']
tmp_mth2(ex_df)
# ex_df.loc[1, 'new'] = ex_df.loc[0, '열1']
print(ex_df)

# exit(0)



############
# 슬라이싱 #
############
print("슬라이싱")
ex_df.index = ["행1", "행2", "행3"]
print(ex_df)
# print(ex_df.loc[0:1, "열1":"열3"])\
print(ex_df.loc["행1":"행2", "열1":"열3"])
"""
이름 지정 슬라이싱, 즉 loc은 시작~끝으로 적용.
   열1  열2  열3
0   1   2   3
1   4   5   6
"""

print(ex_df.iloc[0:1, 0:2]) # 시작~끝-1
"""
iloc으로 슬라이싱하면 시작 ~ 끝-1로 적용됨.
    열1  열2
행1   1   2
"""


# exit(0)
print("행 슬라이싱 \n", ex_df["행1":"행2"]) # 얘는 시작~끝. 모든 열에 대해 특정 행만 뽑고 싶을때 대괄호 슬라이싱
"""
     열1  열2  열3
행1   1   2   3
행2   4   5   6"""

print("열 슬라이싱 \n", ex_df["열1":"열2"]) # 의미 없음
"""열 슬라이싱 
 Empty DataFrame
Columns: [열1, 열2, 열3]
Index: []"""



###############
# 조건 인덱싱 #
###############

print("조건인덱싱")
print(ex_df[ex_df % 2 == 0])


























