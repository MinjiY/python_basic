# 구구단
num = 1
while 1:
    num = int(input('구구단 몇 단을 계산할까요(1~9)? '))
    if num == 0:
        print('구구단 게임을 종료합니다.')
        break
    elif num > 9:
        continue

    for i in range(1, 10):
        print(f'{num}x{i} = {num*i}')
    