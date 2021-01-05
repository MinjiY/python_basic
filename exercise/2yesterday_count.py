'''
yesterday.txt 파일을 읽어서
YESTERDAY 라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday 라는 단어가 몇번 나왔는지 yesterday_lyric.count('Yesterday')
yesterday 라는 단어가 몇번 나왔는지 yesterday+lyric.count('yesterday')
'''


# file = open('yesterday.txt', 'r')
# str1 = 'yesterday'
# yesterday_lyric = file.read()

# file read를 함수로 선언
def file_read(file_name):
    with open(file_name, 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric

# 함수 호출
yesterday_lyric = file_read('yesterday.txt')
str1 = 'yesterday'
print('Number of a word \'YESTERDAY\' , ', yesterday_lyric.upper().count(str1.upper()))      # 기준 str1두고 upper()
print('Number of a word \'Yesterday\' , ', yesterday_lyric.count(str1.capitalize()))         # 첫번째 문자만
print('Number of a word \'yesterday\' , ',yesterday_lyric.count(str1))


