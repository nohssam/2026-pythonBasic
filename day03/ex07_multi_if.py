# 다중 if문
# if 조건식1:
#   조건식1이 참일때 실행할 문장
#   조건식1이 참일때 실행할 문장
# elif 조건식2:
#   조건식1이 거짓 이면서 조건식2는 참일때 실행할 문장
#   조건식1이 거짓 이면서 조건식2는 참일때 실행할 문장
# elif 조건식3:
#   조건식1,2이 거짓 이면서 조건식3는 참일때 실행할 문장
#   조건식1,2이 거짓 이면서 조건식3는 참일때 실행할 문장
# [else:
#   조건식 1,2,3 모두 거짓일때 실행 (나머지)
# ]

# 이름, 국어, 영어, 수학, 점수 받아서  총점, 평균(소숫점 첫째자리까지), 학점을 구하자
name = input("이름 : ")
kor = int(input("국어점수 : "))
eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))

sum = kor + eng + math
avg = sum / 3
hak = ""

if avg >= 90:
    hak = "A학점"
elif avg >= 80:
    hak = "B학점"
elif avg >= 70:
    hak = "C학점"
else:
    hak = "F학점"

print(f'{name=}')
print(f'{sum=}')
print(f'{avg=:.2f}')
print(f'{hak=}')