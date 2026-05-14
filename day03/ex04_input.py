# input : 키보드로 정보를 입력 받아서 처리할 수 있다.
# input으로 들어온 정보는 다 문자열 이다.

name = input('이름 : ')
kor = int(input('국어점수 : '))
eng = int(input('영어점수 : '))
math = int(input('수학점수 : '))

sum = kor + eng + math
avg = sum / 3

# 이름, 총점 ,평균(소수점 2자리까지, 반올림됨) 출력
print(f'{name=}')
print(f'{sum=}')
print(f'{avg=:.2f}')
