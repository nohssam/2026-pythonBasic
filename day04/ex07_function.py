# 함수 : 특정 작업을 수행하는 코드 묶음

# 기본 함수
# 리턴이 있는 함수
def add(a,b):
    return a+b

res = add(5,7)
print(f"{res=}")

# 리턴이 없는 함수
def sub(a,b):
    print(f"{a-b=}")
sub(7,5)
print("-" * 50)

# 지역변수 , 전역변수
x = 100 # 전역변수
def test():
    x = 50
    print(f"함수 안 {x=}")

test()
print(f"함수 밖{x=}")
print("-" * 50)

# global 사용
y = 10
def test2():
    # 함수 안에서 전역변수를 읽기/쓰기 가능하게 하는 예약어
    global y
    y = 99

test2()
print(f"{y=}")
print("-" * 50)

# 기본값 매개변수
def greet(name="손오공"):
    print(f"Hello {name}")


greet("홍길동")
greet()
print("-" * 50)

# 가변 매개변수 (*args)
# 관례상 *args 사용하지만 *number 등 다른 이름도 사용 가능
# 내부 타입은 항상 tuple
def add_all(*args):
    print(f"{args=}, {type(args)=}")
    return sum(args) # 합계 구하는 함수 : sum()

print(add_all(1,2,3,4,5))
print(add_all(1,2,3,4,5,6,7,8,9,10))
print("-" * 50)

def show_all(*args):
    # enumerate란 반복문에서 인덱스와 값을 동시에 가져오는 내장 함수
    for i, arg in enumerate(args):
        print(f" args[{i}] = {arg}, {type(arg)=}")

show_all(1, "hello", 3.14, True, [1,2,3])
print("-" * 50)

# 키워드 매개변수
# 키 와 값 쌍으로 개수 제한없이 받아 딕셔너리로 묶어주는 매개변수
def info(**kwargs):
   print(f"{kwargs=}, {type(kwargs)=}")

info(name="홍길동", age=20, addr='서울')

def introduce(**kwargs):
    for k, v in kwargs.items():
        print(f"{k=}: {v=}")

introduce(name="고길동", age=34, addr='제주도')

# 일반인수 + *args +   **kwargs 함께 사용
def mix (a, *args, **kwargs):
    print(f"{a=}")
    print(f"{args=}")
    print(f"{kwargs=}")

# 반드시 순서는 지켜야 한다.
mix(1,2,3, name="hong", age=20)
print("-" * 50)

# 여러값 반환
def calc(a, b):
    return a+b, a-b

k, y = calc(10,3)
print(f"{k=}, {y=}")
print("-" * 50)

#  함수 재정의 (오버로딩 없음)
def test_func(a):
    print(f"{a=}")


def test_func(a, b):
    print(f"{a=}, {b=}")

# test_func(1) 오류
test_func(1, 10)


