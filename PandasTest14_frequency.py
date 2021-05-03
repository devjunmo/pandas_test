import pandas as pd

df = pd.DataFrame({
                    'A': [
                        'jim',
                        'jim',
                        'jim',
                        'jim',
                        'sal',
                        'tom',
                        'tom',
                        'sal',
                        'sal'],
                    'B': [
                        'a',
                        'b', 
                        'a', 
                        'b', 
                        'b', 
                        'b', 
                        'a', 
                        'a', 
                        'b']
                    })  

df

freq = df.groupby(['A']).count() 
print(freq)

freq = df.groupby(['B']).count() 
print(freq)