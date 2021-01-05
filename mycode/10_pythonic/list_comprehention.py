# 일반적인 for + append

result = []
for val in range(10):
    if val % 2 ==0:
        result.append(val)

print(result)

# List Comprehensions
result2 = [val for val in range(10) if val % 2 == 0]
print(result2)

#번역api 이용해서 노래 가사를 번역하는 코드를 짜볼 것

my_str1 = "Hello"
my_str2 = "World"

result = [i+j for i in my_str1 for j in my_str2 if not ( i==j )]
print(result)



