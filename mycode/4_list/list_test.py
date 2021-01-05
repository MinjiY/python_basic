'''
list 타입을 선언하고 list에 앨리먼트를 추가, 삭제

'''

num_list = [10, 20, 40, 50]

num_list2 = [1, 2, 3, 4, 5]
print(num_list, num_list2)
num_list2 = num_list
print(num_list, num_list2)
num_list.sort()
num_list2 = [1, 2, 3, 4, 5]
num_list.sort()
print(num_list, num_list2)


print(type(num_list), num_list)
print(num_list[0], num_list[0:3])

for num in num_list:
    print(num)

for idx, num in enumerate(num_list):        # 인덱스까지
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
str_list[1] = 'java script'
print(type(str_list), str_list)
print(str_list[1], str_list[2:4])

# 앨리먼트 추가
str_list.append('Cobol')
str_list.insert(1, 'type script')
print(str_list)

del str_list[0]
del str_list[:3]

print(str_list * 2)
print('Scalar' in str_list)
print('java' in str_list)

for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']

for mix in mix_list:
    print(type(mix), mix)

my_list = list('Python')
print(type(my_list), my_list)

my_list2 = 'Hello, Python'.split(',')
print(my_list2)

# packing 과 unpacking

# packing
my_list3 = ['aa', 'bb', 'bb', 'ab']
print(my_list3.index('bb'))
print(my_list3.count('bb'))             # 문자열에서도, 리스트에서도 쓸 수 있다

my_list4 = ['dd', 'ff']


# unpacking
str1, str2 = ['cc', 'dd']
print(my_list3.extend(my_list4))




