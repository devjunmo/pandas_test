import pandas as pd

df2 = pd.DataFrame(columns=['chr', 'start', 'end'])
df2.loc[1] = ["1", "10", "11"]
df2.loc[2] = ['1', '12', '13']
df2.loc[3] = ["1", "13", "14"]
df2.loc[4] = ['2', '14', '15']
df2.loc[5] = ["2", "16", "17"]
df2.loc[6] = ['3', '17', '18']

print(df2)


df2_m = pd.DataFrame(columns=['chr', 'start', 'end', \
                            'class', 'com'])
df2_m.loc[1] = ["1", "10", "11", 'intron', 'hello']
df2_m.loc[2] = ["1", "11", "12", 'exon', 'hi']
df2_m.loc[3] = ["1", "12", "13", 'intron', 'bye']
df2_m.loc[4] = ["1", "13", "14", 'exon', 'heee']
df2_m.loc[5] = ["1", "14", "15", 'exon', 'amc']
df2_m.loc[6] = ["1", "15", "16", 'intron', 'galaxy']
df2_m.loc[7] = ["1", "16", "17", 'notv', 'test']
df2_m.loc[8] = ["1", "17", "18", 'intron', 'py']
df2_m.loc[9] = ["1", "18", "19", 'nonv', 'java']

print(df2_m)

df2['key'] = df2['chr'] + df2['start'] + df2['end']
df2_m['key'] = df2_m['chr'] + df2_m['start'] + df2_m['end']


# df2에다가 df2_m을 붙여보자

result = pd.merge(df2, df2_m, on=['chr', 'start', 'end'], how='left')

print(result)