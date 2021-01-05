# guess game 1~100
import random
guess_number = random.randint(1, 100)
user_number = 0
cnt = 0;
while guess_number != user_number:
    user_number = int(input('임의의 숫자를 입력(1~100): '))
    cnt += 1
    if guess_number < user_number:
        print('숫자가 너무 큽니다.')
    elif guess_number > user_number:
        print('숫자가 너무 작습니다.')
else:
    print(f'정답은 {guess_number}, 총 {cnt}번 만에 맞춤')

