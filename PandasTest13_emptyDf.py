import pandas as pd

df2 = pd.DataFrame(columns=['p_T', 'p_I', 's_T', 's_I'])
df2.loc['mySample'] = ['a', 'b', 'c', 'd']
df2.loc['mySample2'] = ['a1', 'b2', 'c3', 'd5']

df2




empty3 = pd.DataFrame()

empty3.fillna(0, inplace=True)

empty3

empty3.loc['exon', 'snp1'].empty()

empty3.loc['exon', 'snp1'] = empty3.loc['exon', 'snp1'] + 8

empty3

empty3.loc['intron', 'snp2'] = 10 + 9 + 100

empty3

empty3.fillna(0, inplace=True)

empty3


empty3.loc['intron', 'snp1'] = 10 + 90 + 10 # NaN에 값 직접대입은 ok

empty3

empty3.loc['intron', 'snp1']

empty3.loc['intron', 'snp1'] = empty3.loc['intron', 'snp1'] + 10 # 기존값에 더하기 ok
empty3

empty3.loc['exon', 'snp2'] = empty3.loc['exon', 'snp2'] + 10 # NaN에 

empty3