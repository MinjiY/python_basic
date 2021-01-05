# dict 타입
# dict(), { }

lang_dict = {}
lang_dict2 = dict()
print(type(lang_dict), type(lang_dict2))

# dict에 값을 저장
lang_dict[100] = '자바'
lang_dict[200] = '파이썬'
lang_dict[200] = '텐서플로'
lang_dict[300] = 'pytorch'
print(lang_dict)

print(lang_dict[300])
# error: print(lang_dict[400])

value = lang_dict.get(400) # 없는 경우
print(value)

if value:
    print(value)


for k, v in lang_dict.items():
    print(k, v)


lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

los = ['ab','cd','ef']
print(dict(los))

print( 400 in lang_dict)                # key로 있는지 없는지 확인
print( 'pytorch' in lang_dict.values()) # value로 있는지 없는지 확인

print(lang_dict.items())

# zip() 함수
days = ['월요일','화요일','수요일']
fruits = ['사과', '바나나', '딸기']
coffees = ['아메리카노', '라떼', '모카', '믹스']

print(zip(days, fruits, coffees)) #,type(zip(days, fruits, coffees)))

for day, fruit, coffee, in zip(days, fruits, coffees):
    print(day, fruit, coffee)

dict2 = dict(zip(days, fruits))

print(dict(zip(days, fruits)))
print(list(zip(days, coffees)))

for value in list(zip(days, coffees)):
    print(value)

days_tuple = '월요일', '화요일', '수요일'
coffees_tuple = '아메리카노', '라떼', '모카'

print(type(days_tuple))
print(list(zip(days_tuple, coffees_tuple)))
print(dict(zip(days_tuple, coffees_tuple)))

# range() 함수는 iterable 객체를 반환하기 때문에 for ~ in , list() 함수를 사용한다
print(range(10))
print(list(range(1, 10, 2)))


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
ex = {}
