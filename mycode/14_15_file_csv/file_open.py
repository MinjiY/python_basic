# file open /read
with open('i_have_a_dream.txt','r')
    contents = my_file.read()

    # 공백 기준으로 단어를 분리
    word_list = contents.split(" ")
    # 한 줄 씩 분리해서 리스트로 저장
    line_list = contents.split("\n")

print("Total Number of Characters {}".format(len(contents)))
print("Total Number of Words {}".format(len(word_list)))
print("Total Number of Lines {}".format(len(line_list)))

