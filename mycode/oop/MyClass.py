# 클래스 선언
# class MyClass extends Object {} - Java
# class MyClass(Object), class MyClass: - Python
# class MyClass(object):      생략가능 (상속안받을꺼니까 object가 default)
#   pass
class MyClass:
    # constructor 생성자 선언
    def __init__(self):
        # 속성 (attribute) 초기화
        self.num = 100

        # private 속성
        self.__name = 'dooly'

    # method(행위) 선언
    def read_number(self):
        return self.num

    # 부모 클래스(object)가 가진 __str__ 메서드를 재정의함 (규칙임!)
    def __str__(self):       # 객체 주소대신 다른 특정 값을 보고싶을때
        return f'MyClass의 속성 num: {str(self.num)}'

    # getter method __name변수값을 확인하려면 이 메소드를 통해서 확인한다
    # property함수는 method지만 myobj1.name() 하지않는다 ()없이 사용
    @property
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if len(new_name) == 3:
            self.__name = new_name
        else:
            print('새로운 이름의 길이는 3이어야 합니다.')


# 객체를 생성
myobj1 = MyClass()
print(myobj1, type(myobj1))
#print(myobj1.__name)
print(myobj1.name)                  #getter method 호출
myobj1.num = 10
print(myobj1.read_number())

# setter 메소드 생성
myobj1.name = '길동'
print(myobj1.name)
