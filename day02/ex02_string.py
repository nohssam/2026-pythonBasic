# 인덱싱 : 문자열에서 특정 위치의 문자 1개를 꺼내는 것
#         양수 인덱싱 : 0 부터 시작 ,  왼쪽 -> 오른쪽
#         음수 인덱싱 : -1 부터 시작 ,  오른쪽 -> 왼쪽

# 슬라이싱 : 문자열에서 특정 범위를 잘라내는 것
#           [시작위치 : 끝위치(포함안됨)]

# 가변형(Mutable) : 리스트, 딕셔너리, set => 추가, 삭제 , 수정 가능
# 불변형(Immutable) : 문자열, 튜플 => 수정 불가

str = "Hello"
#  H  e  l  l  o
#  0  1  2  3  4
# -5 -4 -3 -2 -1

str = "Hello Python"
print(str[6])  #P
print(str[-2]) #o

print(str[1:3], type(str[1:3]))
print(str[3:1])  # 오류도 아니고 안나옴

print(str[-4:-2])
print(str[-2:-4]) # 오류도 아니고 안나옴

# Hello 만 추출
print(str[0:5])
print(str[:5])  # 처음부터

# Python 만 추출
print(str[6:12])
print(str[6:len(str)]) # len()는 string 길이를 구하는 함수
print(str[6:])  # 끝까지

str = "Hello Python"
print(str[6])
# 문자열은 불변성를 가진다. (수정하려면 오류 발생한다.)
# str[6] = "K"

str = "Hello" # 내용이 수정되는 것이 아니라 새 객체를 만들어서 재할당



