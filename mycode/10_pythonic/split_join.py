# Split과 Join함수

my_str = 'java python Kotlin'
my_list = my_str.split()
print(type(my_list), my_list)

my_str2 = ''.join(my_list)
print(my_str2)

my_str = 'java,python,Kotlin'
my_list = my_str.split(',')
print(type(my_list), my_list)

my_str2 = '/'.join(my_list)
print(my_str2)
'''
선생님 질문이있습니다!
my_str1 = 'java,python,Kotlin'
my_list = my_str1.split(',')
my_str2 = '/'.join(my_list)
이렇게 해서 
'java,python,Kotlin' 문장을 => 'java/python/Kotlin'
으로 바꿨는데 혹시 이거를 바로 바꿀 수 있게 해주는 메소드가 따로있나요??
'a,b'.replace(',','/')
result = my_str.replace(',', '?')
print(result)
'''
words = 'Here are some conventions you should follow to make your code easier to read.'
print(words)

my_list = [[w.upper(), w.lower(), w.title(), len(w)] for w in words]
print(type(my_list), my_list)
for word in my_list:
    print(word)

# enumerate 함수 - for loop를 dict에 저장
for idx, w in enumerate(words):
    print(idx, w)

print(enumerate(words), type(enumerate(words)))
print(list(enumerate(words)))

word_dict = {idx: w for idx, w in enumerate(words, 1)}
print(word_dict)


# zip 함수
print('zip 함수')
my_list1 = [1, 2, 3]
my_list2 = [10, 20, 30]
my_list3 = [100, 200, 300]
print(zip(my_list1, my_list2, my_list3), type(zip(my_list1, my_list2, my_list3)))
print(list(zip(my_list1, my_list2, my_list3)))

for val in zip(my_list1, my_list2, my_list3):
    print(type(val), val, sum(val))

result = [sum(val) for val in zip(my_list1, my_list2, my_list3)]
print(result)

result_dict = {idx: val for idx, val in enumerate(zip(my_list1, my_list2, my_list3))}
print(result_dict)

a, b, c = zip(my_list1, my_list2, my_list3)
print(a)
print(b)
print(c)