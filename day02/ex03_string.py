# 문자열 관련 함수들

str = "Hello Python"

# count(문자열): 문자열의 갯수
print(str.count('o'))  # 2 ('o'의 개수)
print(str.count('x'))  # 0
print('*' * 30)

# 해당 문자 찾아서 위치값(인덱스) 반환 : find, index
# 해당 문자가 여러개 이면 첫번째 문자의 위치 반환
# 없으면 -1 반환(find), 없으면 오류 발생(오류발생)
print(str.find('P'))
print(str.find('K'))  # -1
print('*' * 30)

print(str.index('P'))
# print(str.index('K')) # 오류발생
print('*' * 30)

# 문자열 삽입 : join(리스트나 튜플에서도 사용 가능)
# str이 가지고 있는 문자열 각각의 문자 사이에 해당 글자 삽입
# (마지막글자는 내용이 삽입되지 않는다.)
print('*, '.join(str))

# 소문자를 대문자로 변경 : upper()
print(str.upper())
# 대문자를 소문자로 변경 : lower()
print(str.lower())
# 첫글자만 대문자 나머지는 소문자 : capitalize()
print(str.capitalize())
print('*' * 30)

str = '   hello    '
# 왼쪽 공백 지우기   : lstrip()
# 오른쪽 공백 지우기 : rstrip()
# 양쪽 공백 지우기   : strip()
print(str, len(str))
print(str.lstrip(), len(str.lstrip()))
print(str.rstrip(), len(str.rstrip()))
print(str.strip(), len(str.strip()))
print('*' * 30)

# 문자열 바꾸기 : replace(찾는문자열, 바꿀문자열)
str = "Life is too short"
print(str.replace('Life', "Your leg"))
# 찾은 문자열이 없으면 원본 그대로 나온다.
print(str.replace('Lief', "Your leg"))
print('*' * 30)

# 문자열 나누기 : 중요 => 결과가 list로 나온다.
# split("구분자") : 구분자를 생략하면 스페이스(공백), 탭, 엔터 기준으로 나눠진다.
str = "Life is too short"
print(str.split(), type(str.split()))
print('*' * 30)

str = "Life,is,too,short"
print(str.split(), type(str.split()))
print(str.split(","), type(str.split()))
print('*' * 30)

str = "Life is too short"
# 특정 문자열로 시작하는지 확인 : startswith => 맞으면  True, 틀리면 False
print(str.startswith('Life'))
print(str.startswith('Lief'))

# 특정 문자열로 끝나는지  확인 : endswith => 맞으면  True, 틀리면 False
print(str.endswith('short'))
print(str.endswith('long'))
print('*' * 30)

user_input = "  Hong@Gmail.Com   "
email = user_input.strip().lower()
print(email)

# 유효성 검사
if '@' in email and email.endswith('.com'):
    print("유효성 검사 통과 O")
else:
    print("유효성 감사 통과 X")

