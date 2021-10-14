
tmp_dict = dict()

tmp_dict['key1'] = ['val1']

tmp_dict

tmp_dict['key1'].append('val2')

tmp_dict

tmp_dict['key1']


tmp_dict['key2'] = ('val1')

# tmp_dict['key2'].append('val2') # err 

tmp_dict # {'key1': ['val1'], 'key2': 'val1'}

type(tmp_dict['key2']) # str


# 튜플로 key, value 가능

test_key_tup = (1, 2, 'a')
test_val_tup = ('a', 'b')

tmp_dict[test_key_tup] = test_val_tup

tmp_dict

tmp_dict[test_key_tup]




# inner dict

inner_dict = dict()

inner_dict['in_key1'] = dict()

inner_dict['in_key1'][('my', 'tup', 'key')] = ('my', 1, 'val')

inner_dict


inner_dict['in_key1'][('my2', 'tup2', 'key2')] = ('my2', 2, 'val2')

inner_dict

inner_dict['in_key1'][('my2', 'tup2', 'key2')]

type(inner_dict['in_key1']) # <class 'dict'>


# 리스트 두개 더하기

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst1 + lst2

lst3