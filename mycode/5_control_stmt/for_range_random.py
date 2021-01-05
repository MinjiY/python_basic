'''
range() 함수
'''

print(range(10), range(1, 11))    #시작 값 안주면 0부터
for val in range(1, 10, 2):
    print(val)
else:
    print('for loop 종료')

print('while 문')
i = 0
while i < 10:
    print(i)
    i += 2
else:
    print('while 문 종료')

wish_travel_cities = {
    '일본': '도쿄',
    '한국': '서울',
    '미국': '뉴욕',
    '한국': '부산'
}

print(wish_travel_cities.keys())
print(wish_travel_cities['일본'])
print(wish_travel_cities.values())
print(wish_travel_cities.items())
for key in wish_travel_cities.keys():
    print(f'{key}의 {wish_travel_cities[key]}를(을) 여행하고 싶어요')
    #pass

for k, v in wish_travel_cities.items():
    print(f'{k}의 {v}를 방문하고 싶어요')

import random

for val in range(10):
    random_value = random.randint(1, 100)
    print(random_value)


print(random.random())
print(random.choice([1, 2, 3, 4, 5]))

