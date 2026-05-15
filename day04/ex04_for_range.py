# range(시작, 끝) : 시작 ~ 끝-1 까지 숫자 생성

su = range(1,11)  # 1-10

print(f"{su}")
print(f"길이 = {len(su)}")
print(f"타입 = {type(su)}")
print('-' * 50)


for i in range(1,11):
    print(f"{i}", end=" ")
print()
print('-' * 50)

for i in su:
    print(f"{i}", end=" ")
print()
print('-' * 50)

# 7단
for i in range(1,10):
    print(f"7 * {i} =  {7 * i}")
print('-' * 50)

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()
print('-' * 50)

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}", end="      ")
    print()
print('-' * 50)

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} x {i} = {i * j}", end="      ")
    print()
print('-' * 50)