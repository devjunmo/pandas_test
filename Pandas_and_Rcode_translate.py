import pandas as pd
import re
from numpy import nan as NA

df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Dave','Ellen','Frank'],
                   'age': [24,42,18,68,24,30],
                   'state': ['NY','CA','CA','TX','CA','NY'],
                   'point': [64,24,70,70,88,57]}
                  )
"""      name  age state  point
0    Alice   24    NY     64
1      Bob   42    CA     24
2  Charlie   18    CA     70
3     Dave   68    TX     70
4    Ellen   24    CA     88
5    Frank   30    NY     57"""

# R의 is.na 필요한가? --> R은 str_extract시 없으면 NA 뱉는다. 파이썬도 그러한가?


# 삼항 연산자, 참리턴 if 조건 else 거짓리턴
# print(100 if 10>9 else 0) # 100


# str_extract와 매칭되는 메소드
df["ext"] = df.name.str.extract(r'(li)')
# df["ext2"] = df.name.str.extract(r'li') # 에러
print(df)

# is.na와 매칭되는 메소드
s1 = pd.Series([1,2,3,NA])
print(pd.isnull(s1))
print(s1.isnull())

# 완벽히 일치하는 문자열 찾기 --> 조건 인덱싱으로 처리


# new 컬럼에 넣기 -> 간편하게 대입

# 컬럼 제거하기 <- 메모리 free

# str_replace_all

# regexpr -> 코드에서 쓴 이유 = 사실 별 의미 없음. 걍 str.extract로 가능해보임.

# paste -> 플러스 연산자로 처리 가능.

# 확장에 대한것 어떻게 처리할것인가




# 정규 표현식

# 반복 사용시 컴파일 해놓는게 속도면에서 유리할수 있다고 함.

# re 모듈 메타문자 $()*+.?[\^{|
print("정규 표현식 연습")
print("?"); print('?') # ok


# 결론 = 원래는 \\?여야 하는듯 하나, r없이 \? 해도 보정됨. 왜인지는 모르겠다.
# <re.Match object; span=(0, 15), match='Why so serious?'>
matchObj1 = re.search('Why [a-z]o serious\?', 'Why so serious?'); print(matchObj1)
# <re.Match object; span=(0, 15), match='Why so serious?'>
matchObj6 = re.search('Why [a-z]o serious\\?', 'Why so serious?'); print(matchObj6)

# <re.Match object; span=(0, 15), match='Why so serious?'>
matchObj2 = re.search(r'Why [a-z]o serious\?', r'Why so serious?'); print(matchObj2)

# <re.Match object; span=(1, 16), match='Why so serious?'>
matchObj3 = re.search(r'(Why [a-z]o serious\?)', r'(Why so serious?)'); print(matchObj3)

# <re.Match object; span=(0, 14), match='Why so serious'>
matchObj4 = re.search(r'Why [a-z]o serious?', r'Why so serious?'); print(matchObj4)

# <re.Match object; span=(1, 15), match='Why so serious'>
matchObj5 = re.search(r'(Why [a-z]o serious?)', r'(Why so serious?)'); print(matchObj5)

matchObj6 = re.search('Why [a-z]o serious\\?', 'Why so serious?'); print(matchObj6)





















