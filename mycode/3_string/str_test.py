'''
문자열 관련 내용들
'''
# escape 문자
greet = 'Hello' * 4 + '\n'
end = '\tGood \'bye\' !!'
end2 = "\t Good 'Morning' ??"
print(greet+end+end2)

# bool 하고 str 타입은 다르다
is_flag = True
my_str = 'True'

print(type(is_flag), type(my_str))

if not is_flag:
    print(my_str)


# 문자열 인덱스(오프셋)
greeting = 'Hello world'
print('문자열 길이: {0}, 0번째 인덱스 값은 {1}'.format(len(greeting), greeting[0]))
print('0번째 인덱스 값을 {1} , 문자열의 길이 {0}'.format(len(greeting), greeting[0]))

# 3.6버전 이후 생긴거
print(f'문자열 길이: {len(greeting)}, 0번째 인덱스 값: {greeting[0]}')


# 문자열 인덱스 슬라이싱 (end값은 exclusive : 0 1 2 3 4 출력
# [start:end:step] step은 default로 1
print(f'greeting[0:5] = {greeting[0:5]}')
print(f'greeting[0:11] = {greeting[0:11]}')
print(f'greeting[:5] = {greeting[:5]}')
print(greeting, greeting[:])
print(greeting[0:5:2])

# 음수 값의 인덱스
print(f'greeting[-1:] {greeting[-1:]}')

# 문자열이 역순으로 바뀐다
print(f'greeting[::-1] = {greeting[::-1]}')

# 문자열 함수
word = 'Good manufacturing Practice Good'
print(word)
print(word.upper())
result = word.upper()
print(word, ' ', result)
print(f'소문자로 변환 = {word.lower()}')
print(word.title())
print(word.find('G'))
print(word.rfind('G'))
print(word.count('n'))
print(word.count('G'))

word_list = word.split()
print(word_list, type(word_list))


word2 = 'Good/manu/facturing/Practice/Good'
print(word2.split('/'))

word3 = ' Hello python '
print(len(word3), len(word3.strip()), word3.strip())
print(len(word3.rstrip()), word3.rstrip())

print(word.startswith('G'))
print(word.endswith('G'))

for val in word:
    print(val, word.count(val))

print(word_list)
for w in word_list:
    print(w)


