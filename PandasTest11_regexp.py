import pandas as pd
import re
import numpy as np
import classTest


# print(f"{0x21}, 0x21")
# print(f"{str(0x7E)}, 0x7E")
#
# print(bytes.fromhex("7E").decode("ASCII"))
#
# exit(0)


# df = pd.DataFrame({'name': ['iu/ml','Bob','Chaarlie','Daaave','Ellen','Fraank']})
# print(df)
# df = df.drop(['name'], axis=1)
# print(df)
# """
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3, 4, 5]"""
# # exit(0)

# df = pd.DataFrame({'name': ['iu/ml','Bob','Chaarlie','Daaave','Ellen','Fraank']})
# print(df)
# # df = df.drop(['name'], axis=1)
# classTest.JustTest(1, df)
# print(df) # 저쪽 클래스에서 inplace=True 넣어주면 empty df 만들기 된다.
#
# exit(0)

# df = pd.DataFrame({'name': ['iu/ml','Bob','Chaarlie','Daaave','Ellen','Fraank']})
# print(df)
# df = df.drop(index=0) # call by ref 주의하시고, row가 디폴트.
# print(df)
# exit(0)

# df = pd.DataFrame({'name': ['iu/ml','Bob','Chaarlie','Daaave','Ellen','Fraank', np.nan]})
# print(df)
# df = df.dropna()
# print(df)
# exit(0)

my_inputs = pd.read_csv(r'C:\test_data\test_result.csv', encoding='CP949')
print(my_inputs)
print(type(my_inputs))

# exit(0)
my_filter = pd.read_csv(r'C:\test_data\filters_backup.csv', encoding='CP949')

print(my_filter)
print(type(my_filter))
# exit(0)
# print(type(df['name']))



#
# p = re.compile(r'a')
# print(p) # re.compile('a')
# print(df['name'].iterrows()) # RangeIndex(start=0, stop=6, step=1)

# print(p.search(df['name'].index))



# test1 = p.search('Apple')
# test2 = p.search('Berry')

#
# print(test1); print(test2)
# print('값은', test1.group(), '/ 타입은', type(test1.group())) # 값은 a / 타입은 <class 'str'>
# print('값은', test2.group(), '/ 타입은', type(test2.group())) # 값은  / 타입은 <class 'str'>

# print(df['name'])

# for name in df['name']:
#     # print(name, type(name)) # str 타입으로 나옴
#     test3 = p.search(name)
#     if test3: # None이 아닐때
#         print('Match found...\n ', test3.group())
#     else:
#         print('No match')
#     # print(test3.group())

# print(df.replace('()li()', r'\1LI\2', regex=True))



# exit(0)

# df['name'].replace(None, p.search(df['name']), regex=True, inplace=True)



# <기본 포멧은 아래와 같이 하자... >
# unit[0] unit[1] 코딩 해야함. 필터. csv에는 공백단위로 작성. 예시는 unit 이나 comment 코드)
# sep 기준 중복 cut하는 작업도 코딩해야 함. 예시는 cat-general 추출의 weak_positive (마지막 컬럼 sum 상황에서..)
count = 0

# print("콕찝기", my_inputs.loc[12, 'res'])
# print("콕 찝기", my_filter.loc[1, "rm_data"])
# exit(0)
# 필터루프 돌렸다고 가정 for filter in filters:
# 만약 필터에 [:print:]가 있다면, [:print:]를 ㅁ로 replace한다.
# ^NA[{bytes.fromhex("20").decode("ASCII")}-{bytes.fromhex("7E").decode("ASCII")}]+


# test_patt = re.compile(rf'{my_inputs.loc[13, "res"]}') # iu\\/ml는 안되고, iu/ml는 된다.
# test_patt = re.compile(rf'{my_filter.loc[11, "rm_data"]}') # [:alpha:]+\\d+  // ok!
# test_patt = re.compile(rf'^\w+-\d+') # [:alpha:]+\\d+  // ok!
# test_patt = re.compile(rf'^\d+[a-zA-Z]+\d+') # // ok!
# test_patt = re.compile(rf'^20\d\d-') # // ok!
# test_patt = re.compile(rf'\\') # // ok! 필터는 \\, res는 \ --> 좀 신기하다
# print(bytes.fromhex("7E").decode("ASCII"))
# test_patt = re.compile(rf'{my_filter.loc[5, "rm_data_partially"]}') # [:alpha:]+\\d+  // ok! [:alpha:]
# test_patt = re.compile(rf'^NA[{bytes.fromhex("20").decode("ASCII")}-{bytes.fromhex("7E").decode("ASCII")}]+') # [:print:]+

# test_str = '^NA[{bytes.fromhex("20").decode("ASCII")}-{bytes.fromhex("7E").decode("ASCII")}]+'
# test_patt = re.compile(test_str)

# test_patt = re.compile(my_filter.loc[6, "rm_data_partially"]) # ok
# test_patt = re.compile(my_filter.loc[6, "rm_data_fully"]) # 필터에 \\, res에 \   --> ok
# test_patt = re.compile(rf'^NA.+') # ok
# test_patt = re.compile(rf'^[가-힣][가-힣][가-힣]+') # ok

# test_patt = re.compile(my_filter.loc[1, "separate_txt_pm"]) # ok

# test_patt = re.compile(my_filter.loc[1, "ext_sign_pm"]) # ok
# test_patt = re.compile('mg/12h[a-z]*') # ok
# test_patt = re.compile(rf'ba|bal.*')
# test_patt = re.compile(rf'bal.+|bal') # 우선순위가 적용됨. 이거로 하면 되겠네;

test_patt_think = re.compile(r"[*][*][*]")
# test_patt = re.compile(rf'\[+')
# test_patt = re.compile(rf']+')
# test_patt = re.compile(rf'/')
# test_patt = re.compile(rf'\(')
# test_patt = re.compile(rf'\)')
# test_patt = re.compile(rf'\s+')
# test_patt = re.compile(rf'[N]/[A]]')

# my_str = "\s+"
# my_str = "\d+"
my_str = "ba.+"
test_patt = re.compile(rf'{my_str}')


# test_search = test_patt.search(my_input[0])
#
# print(test_patt)
# exit(0)
# df['new'] = my_inputs.res.str.extract(test_patt.)
# print(df)
# exit(0)

def test_mtd(my_input):
    global count
    test_search = test_patt.search(my_input[0])
    if test_search:  # None이 아닐때
        print('Match found...\n ', test_search.group(), "count: ", count)
        print('.group()의 자료형은, ', type(test_search.group())) # .group()의 자료형은,  <class 'str'>
        print("인덱스는...", index, "인덱스 타입은..", type(index))
        count += 1
        # 여기에 추가 처리 하면 댐. replace나.. strExtract나...
        # extract, new_col넣고, replace_all() 하는식으로 한방에 그때그때

    else:
        print('No match...', "count: ", count)
        count += 1


for index, my_input in my_inputs.iterrows():
    # print(my_input[0]) # 지가 알아서 인덱스 증가 됨.
    test_mtd(my_input)
    # test_search = test_patt.search(my_input[0])
    # if test_search:  # None이 아닐때
    #     print('Match found...\n ', test_search.group(), "count: ", count)
    #     print("인덱스는...", index, "인덱스 타입은..", type(index))
    #     count += 1
    #     # 여기에 추가 처리 하면 댐. replace나.. strExtract나...
    #     # extract, new_col넣고, replace_all() 하는식으로 한방에 그때그때
    #
    # else:
    #     print('No match...', "count: ", count)
    #     count += 1
    # print(test3.group())
exit(0)
# print(df)

# print(df.replace('()li()', r'\1LI\2', regex=True))