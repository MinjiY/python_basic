def add(x, y):
    return x+y

print(add(10, 20))

add2 = lambda x, y: x + y
print(add2(10, 20))
print((lambda x, y: x + y)(10, 20))
print((lambda x: x ** 2)(10))
'''
 map(함수, list) 함수
'''
print('map 함수')
double_val = lambda x: x**2
print(double_val(2))

my_list = [1, 2, 3, 4, 5]
# for loop를 사용해서 함수호출
result_list = []
for val in my_list:
    print(double_val(val))
    result_list.append(double_val(val))
print(result_list)
# 위에처럼하면 복잡하니까

result = map(double_val, my_list)
print(type(result), result)     #객체로 결과가 나와서 아래처럼 확인

result = list(map(double_val, my_list))
print(result)


# my_list를 순회(iterate) 하면서 값을 제곱값으로 반환하는 함수를 호출한다.
# list로 변환하야 값을 확인할 수 있음
result = list(map(lambda x: x**2, my_list))
print(result)


# [1, 2, 3, 4, 5], [10, 20, 30, 40, 50] 두개의 리스트의 값을 더하기
# [11, 22, 33, 44, 55]
# lambda 함수와 map 함수를 사용해서
add = lambda x, y: x+y
print(add(1, 10))
my_list1 = [1, 2, 3, 4, 5]
my_list2 = [10, 20, 30, 40, 50]
result = list(map(add, my_list1, my_list2))
print(result)

result = list(map(lambda x, y: x+y, my_list1, my_list2))
print(result)

# 짝수만 제곱하는 함수
double_even = lambda x: x**2 if x%2 == 0 else x
print(double_even(4), double_even(5))
# list를 순회하면서 double_even을 콜
print(list(map(double_even, my_list1)))
print(list(map(lambda x: x**2 if x%2 == 0 else x, my_list1)))

map_obj = map(double_even, my_list1)
print(next(map_obj), next(map_obj))


'''
reduce() 함수     map과 마찬가지로 인자에 함수들어감
'''

from functools import reduce

add2 = lambda x, y: x+y
print(add2(10, 20))

result = reduce(add2, my_list1)
print(result, type(result))
result = reduce(lambda prev, curr: prev+curr, my_list1)
print(result)

'''
filter() 함수
'''
print('filter() 함수')
my_len = lambda my_str: len(my_str) > 6
print(my_len('hello'), my_len('mypython'))

my_list_str = ['hello', 'mypython', 'Machine', 'Deep', 'DataScience']
# 6글자 이상 문자열만 리스트에 저장하기
result = filter(my_len, my_list_str)
print(result, list(result))

'''
질문이 있습니다!
map()이랑 reduce() 차이점을 잘 모르겠는데요
reduce()에서 초기값을 줄수 있다는 것 빼면 map()과 동일하게 사용할 수 있는 건가요?
BinaryOperator == reduce
reduce() 인자의 메소드는 인자는 2개이상
map() 인자의 메소드는 인자가 1개여도 ㄱㅊ

reduce() => int로 반환
map() => object로 반환
'''











