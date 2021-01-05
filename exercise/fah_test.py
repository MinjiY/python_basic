# 2. import 모듈명 as alias
# import exercise.fahrenheit as fah
# 3. from 모듈명 import 함수명
# from exercise.fahrenheit import fah_convert
# 4. from 모듈명 import *
from exercise.fahrenheit import *


celsius = float(input('변환하고 싶은 섭씨 온도를 입력해주세요:\n'))
# 2번
# result = fah.fah_convert(celsius)
result = fah_convert(celsius)

print('섭씨 온도: ', celsius)
# print('화씨 온도: ', round(fahrenheit, 2))
print('화씨 온도: {:.2f}'.format(result))
print(sayHello('파이썬'))




