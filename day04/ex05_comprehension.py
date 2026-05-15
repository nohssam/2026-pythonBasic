# 컴프리헨션(Comprehension) : 대괄호([]) 등을 활용해서 반복문(for)과 조건문(if)을
# 한 줄로 축약해, 리스트, 딕셔너리, 집합 등의 자료구조를 직관적이고 간결하게 생성하는 문법

# 리스트 컴프리헨션
# [ 표현식 for 변수 in 반복가능객체]

su = [1,3,5,7,9]
res = []

for i in su:
    res.append(i*3)

print(f"{su=}")
print(f"{res=}")
print("-"*50)

su2 = [1,3,5,7,9]
res2 = [ i*3 for i in su2 ]
print(f"{su2=}")
print(f"{res2=}")

# range(10) : 0-9
res3 = [ i for i in range(10) if i % 2 == 0]
print(f"{res3=}")

# 짝수면 'even', 홀수이면 'odd'
res4 = [ 'even' if i%2==0 else 'odd' for i in range(5)]
print(f"{res4=}")

# 대문자로
words = ["hello", "world", "python"]
res5 = [ i.upper() for i  in words]
print(f"{res5=}")

# 문자길이 6글자 이상
res6 = [ i for i in words if len(i) >= 6]
print(f"{res6=}")
