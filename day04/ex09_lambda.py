# lambda 함수 : def 없이 한 줄로 만드는 익명함수
# 기본 구조 ; lambda 매개변수 : 반환값

#일반함수
def add(x,y):
    return x + y

# lambda
add2 = lambda x,y: x + y

print(add(10,3))
print(add2(10,3))

# 매개변수가 없을때
hello = lambda : "Hello Python"
print(hello())

# 매개변수 있을 때
hi = lambda msg: f"{msg}님 환영합니다."
print(hi("hong"))


