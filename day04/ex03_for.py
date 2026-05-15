# for => 반복문

# for 변수 in 자료형(list, tuple, set, dict, string) :
#      실행문


# 1. list
t_list = ["one", "two", "three", "four", "five"]

for i in t_list:
    print(f"{i}님 ^^")

print("*" * 50)

# 2. tuple
t_tuple = ("red", "green", "blue", "yellow")

for i in t_tuple:
    print(f"{i}님 ^^")

print("*" * 50)

# 3. set
t_set = {"둘리","공실이","마이콜"}
for i in t_set:
    print(f"{i}님 환영")

print("*" * 50)

# 4. dice
t_dict = {
    "name": "park",
    "age": 24,
    "phone": "010-7979-9797",
    "height": 181.75
}

# value 출력
for i in t_dict.values():
    print(f"{i}")
print("*" * 50)

# key  출력
for i in t_dict.keys():
    print(f"{i}")
print("*" * 50)

# (key, value) 출력
for i in t_dict.items():
    print(f"{i}")
print("*" * 50)

for k, v in t_dict.items():
    print(f"{k}: {v}")
print("*" * 50)

# **언패킹: 리스트, 튜플 등의 자료구조에서 값을 꺼내 여러 변수에 한번에 할당하는 문법
t_list = [(1,2), (2,4), (3,6)]
for i, j in t_list:
    print(f"{i=} , 타입={type(i)}")
    print(f"{j=} , 타입={type(j)}")
    print("*" * 50)

# 문자열 반복
msg = "Python Hello"

for i in msg:
    if i == "o":
        continue
    print(f"{i}", end=" ")
print()









