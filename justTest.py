import pandas as pd
import classTest

# lst = [1, 2, 3, 4, 5]
#
# [print(l) for l in lst if l % 2 == 0]
# # 4
# # 2
#
# # [if l % 2 == 0 print(l) for l in lst] # 이거 안댐.
#
# k = [l for l in lst if l % 2 == 0]
# print(k) # [2, 4]
#
#
#
# test_str = "my#mys#myname"
#
# tmp_list = test_str.split('#')
# print("tmp_list =", tmp_list)




# test_csv = pd.read_csv('test_result2.csv', encoding='CP949')
# print(test_csv)
#
# classTest.JustTest(1, test_csv)
#
# print(test_csv)



t_list = [1, 2, 3]

print(type(t_list[3]))


exit(0)


# "A|B|C a b c" 알고리즘
tmp_string = "A|B|C a b c"

tmp_list1 = tmp_string.split('|')
print(tmp_list1) # ['A', 'B', 'C a b c']

tmp_string2 = tmp_list1[len(tmp_list1)-1]
print(tmp_string2) # C a b c

tmp_list2 = tmp_string2.split(' ')
print(tmp_list2) # ['C', 'a', 'b', 'c']

tmp_list1.pop()
print(tmp_list1)

my_list = tmp_list1 + tmp_list2
print(my_list)

last_target_idx = int((len(my_list)/2)-1) # 추출한 요소 마지막 인덱스
first_translate_idx = last_target_idx + 1 # 번역할 요소 첫 인덱스

tmp_dict = dict()
count = 0
for i in range(last_target_idx+1):
    print(i) # 0 1 2
    tmp_dict[my_list[i]] = my_list[first_translate_idx]
    first_translate_idx += 1

print(tmp_dict) # {'A': 'a', 'B': 'b', 'C': 'c'}

