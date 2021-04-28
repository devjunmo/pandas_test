import pandas as pd

ex_df = pd.DataFrame([[1,2,3],
                      [4,5,6],
                      [7,8,9]], index=["1", "행2", "행3"], columns=["열1", "열2", "열3"])

poped = ex_df.pop('열2')

# print(ex_df)
print(poped)
print(type(poped)) # <class 'pandas.core.series.Series'>

print(poped['1']) # 2

def test_call_by_value(series):
    series['1'] = 10

test_call_by_value(poped)

print(poped['1']) # 10 // c b b ok
