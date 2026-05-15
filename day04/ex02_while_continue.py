# continue : 아래 코드를 실행하지 않고 다시 반복문 처음으로 돌아 간다.

# 1-10까지 출력 중 4를 제외 시키자
cnt = 0

while cnt < 10:
    cnt += 1
    if cnt == 4:
        continue  # 아래 문장을 하지 않고 반복문 처음으로 간다.

    print(f"{cnt}", end=" ")
print()

# 1-10 홀수만 출력하자
cnt = 0

while cnt < 10:
    cnt += 1
    if cnt % 2 == 0:
        continue

    print(f"{cnt}", end=" ")
print()