import pandas as pd

df2 = pd.DataFrame(columns=['p_T', 'p_I', 's_T', 's_I'])
df2.loc['mySample'] = ['a', 'b', 'c', 'd']
df2.loc['mySample2'] = ['a1', 'b2', 'c3', 'd5']

df2