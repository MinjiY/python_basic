'''
나이 = 현재년도 - 태어난 년도 +1
태어난 년도를 입력 받음 input()
'''
from datetime import datetime as dt          #datetime 을 컨트롤 누른 상태에서 클릭하면 datetime.py로 이동
# 현재년도 datetime 클래스에 선언된 today() 메서드를 호출

birth = int(input('태어난 년도 입력: '))

current_year = dt.today().year
age = current_year - birth+1

if 17 <= age < 20:
    print('고등학생 입니다.')
elif (age <= 20) and (age <= 27):
    print('대학생')
else:
    print('학생이 아닙니다.')



# 메일로 guess게임
# 구구단 보내기 , 이차원리스트 (사람별 평균계산)
# 1월 1일 12시까지 63p 64p

# 1월 11일 django
# html, css, javascript(조금)
# 휴강기간동안 html css javascript 전반적으로 어떤건지 이해해오기 bootstrap이 뭔지
# http 에서 GET방식과 POST 방식의 차이점은 무엇인지, 간단하게 코드작성
# 나도코딩, 조코딩, 테크보이워니 (유튜브)
