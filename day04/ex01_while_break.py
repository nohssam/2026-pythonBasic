# break : 반복문 탈출

coffee = 10

while True:
    print(f"돈을 받았으면 커피를 줍니다.")
    coffee -= 1
    print(f"남은 커피의 양은 {coffee}개 입니다.")

    if coffee == 0:
        print(f"커피가 없네요, 판매 중지 합니다.")
        break # 반복문 탈출

print('*' * 50)
