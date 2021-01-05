'''
# stack  append() & pop()
a = [1, 2, 3, 4, 5]
a.append(10)
a.append(20)
print(a.pop())          # 20
print(a.pop())          # 10


# queue  append() & pop(0)
a.append(10)
a.append(20)
a.pop(0)                # 1
a.pop(0)                # 2


# set
s = set([50, 1, 29, 4, 15, 28])              # 중복 불허
print(s)
s.add(1)                        # add() : 원소 하나만 추가
print(s)
s.remove(50)                    # remove() : 인덱스 x 원소 직접
print(s)
s.update([20, 30, 40])          # update() : 리스트를 추가
print(s)

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))      # intersection() : 교집합
print(s1&s2)
print(s1.difference(s2))        # 차집합
print(s1-s2)

# Dictionary
pythons = {'Chapman':'Graham', 'Cleese':'John', 'Johns':'Terry', 'Palin':'Michael'}
print('Chapman' in pythons)         # key 찾는거만 할 수 있음
print('Cleese' in pythons)
print('Michael' in pythons)

print(pythons.keys())
print(pythons.values())
print(pythons.items())

# zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee','tes','beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
    print(day,": drink", drink, "-eat",fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi','Mardi','Mercredi'

print(list(zip(english, french)))
print(dict(zip(english,french)))


spam = {'name': 'Pooka', 'age':5 }
if 'color' not in spam:
    spam['color'] = 'black'

print(spam.setdefault('color','black'))
print(spam)

print(spam.setdefault('color','white'))
print(spam)

'''

message = ' Hello world python!'
print(message.upper())
print(message.lower())
print(message.rfind('w'))
print(message.startswith('world'))
print(message.endswith('!'))

print(message.strip())              # 양쪽 공백
print(message.rstrip())             # 오른쪽 공백
print(message.lstrip())             # 왼쪽 공백
a = 'aaminjiaajaehyukaa'
b = a.split('aa')
if a.startswith('aa'):
    b.pop(0)
if a.endswith('aa'):
    b.pop()
print(b)
