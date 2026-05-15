# 일반매개변수, 기본값있는 매개변수 같이 있으면
# 기본값있는 매개변수는 맨 뒤에
def say(name, age, gender=True):
    print(f"이름은 {name} , 나이는 {age}")
    if gender:
        print(f"성별은 남성")
    else:
        print(f"성별은 여성")

# 순서가 잘못 되었다.
# def say2(name, gender=True, age):
#     print(f"이름은 {name} , 나이는 {age}")
#     if gender:
#         print(f"성별은 남성")
#     else:
#         print(f"성별은 여성")

say("hong", 24, False)
say("kang", 18, True)
say("park", 12)
