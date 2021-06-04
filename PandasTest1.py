import pandas as pd
import numpy as np


ex_df = pd.DataFrame([[1,2,3],
                      [4,5,6],
                      [7,8,9]], index=["행1", "행2", "행3"], columns=["열1", "열2", "열3"])

print(ex_df) # 예상대로 출력
# print(ex_df["행1"]) # 에러
tmp = ex_df.columns
print(tmp)
print([i.title() for i in tmp])

# exit(0)
print(ex_df["열1"])
"""
행1    1
행2    4
행3    7
Name: 열1, dtype: int64
"""

ex_df["new열1"] = [10, "test", -9]
print(ex_df) # 예상대로 출력
"""
    열1  열2  열3 new열1
행1   1   2   3    10
행2   4   5   6  test
행3   7   8   9    -9 """

ex_df.loc['행1', 'new_empty열'] = 10
ex_df

# ex_df["new열2_over"] = [10, "test", -9, 10] # 에러
# print(ex_df)

ex_df.insert(loc=0, column="열삽입", value=[9,9,9])
print(ex_df)
"""
    열삽입  열1  열2  열3 new열1
행1    9   1   2   3    10
행2    9   4   5   6  test
행3    9   7   8   9    -9
"""































