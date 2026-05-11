# f-string은 python에서 문자열 안에 변수나 표현식을 직접 넣을 수 있는 기능

print(f"Hello World")

name= "홍길동"

# 여러줄
msg = f"""
이름 : {name}
환영합니다.
"""
print(msg)

name = "둘리"
age = 17

# 한줄
print(f"이름:{name},  age:{age}")

su1 = 10
su2 = 3

#  표현식 가능(연산 가능)
print(f"합: {su1 + su2}")
print(f"차: {su1 - su2}")
print(f"곱: {su1 * su2}")
print(f"나누기: {su1 / su2}")
print(f"몫: {su1 // su2}")
print(f"나머지: {su1 % su2}")
print()

# 함수도 가능
def hi():
    return "Hi World"

print(f"{hi()}")
print("*" * 50)

# 변수이름 + 값 같이 볼때 (디버깅)
x = 5
y = 10

print(f"x={x}, y={y}")
print()
print(f"{x=}, {y=}")

# 소숫점 처리(반올림)
k1 = 3.144592
print(f"{k1:.2f}")

k2 = 3.145592
print(f"{k2:.2f}")

# 숫자 코마
num = 1000000
print(f"{num:,}")

# 원단위 절삭
price = 1234567
result = (price // 10) * 10
print(f"{result:,}")