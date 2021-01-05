kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]
# print(midterm_score)
# print(midterm_score[0])
# print(midterm_score[0][3])

student_score = [0, 0, 0, 0, 0]

for subject in midterm_score:
    print(subject)
    i = 0
    for score in subject:
        student_score[i] += score
        i += 1
else:
    print(f'학생별 합계 점수 = {student_score}')

    # 평균을 계산(unpacking 사용)
    a, b, c, d, e = student_score
    student_average = [int(a/3), int(b/3), int(c/3), int(d/3), int(e/3)]
    print(f'학생별 평균점수 = {student_average}')

