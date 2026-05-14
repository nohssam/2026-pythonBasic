# while 문
# 초기식
# while 조건식:
#       조건식이 참일때 실행할 문장
#       조건식이 참일때 실행할 문장
#       증감식

# 1-10까지 출력
cnt = 1
while cnt <= 10:
    # 줄변경하지 말고 뛰어쓰기 하자
    print(f'{cnt}' , end=' ')
    cnt += 1
print()

# 1-10까지 짝수 출력
cnt = 1
while cnt <= 10:
    if cnt % 2 == 0:
        print(f'{cnt}', end=' ')
    cnt += 1
print()

prompt = """
 1. Add
 2. Del
 3. List
 4. Quit
 
 Enter your choice: """

cnt = 0
while cnt != 4:
    print(prompt)
    cnt = int(input())
    print(f"당신의 선택 : {cnt}")

print("수고하셨습니다.")




