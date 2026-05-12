# 튜플은 몇가지를 제외하고 리스트와 거의 같음
# 불변성(수정 안됨) ,  표현 : (항목, 항목, 항목)

t1 = (1,2,3)
t2 = ('a','b','c')
t3 = (1, 'hello', 3.14, True)

print(t3, type(t3))

lis = [3]
print(lis, type(lis))

# 튜플 주의 사항
# 자료형 ; int => tuple x
t4=(3)
print(t4, type(t4))

# 자료형 : tuple
t5=(3,)
print(t5, type(t5))

# 빈 튜플 생성 가능, 빈 리스트 생성 가능
lis2 = []
print(lis2, type(lis2))

t6=()
print(t6, type(t6))

# () 생략
t7 = 1,2,3,4,5
print(t7, type(t7))

# 튜플은 항목 삭제, 수정 안됨 (불변형), 추가는 직접 추가는 안됨(새 튜플을 만드는 방식은 가능)
tup = (1,2,3,4,5)

# 직접 추가 안됨
# tup.append(6)

# 새 튜플을 만드는 방식은 가능 (기존튜플 = 기존튜플 + 새 튜를)
tup = tup + (6,7,8,9)
print(tup, type(tup))

# 하나추가할때 조심
tup = tup + (10,)
print(tup, type(tup))
print('*' * 30)

# 튜플를 리스트로 변경한 후 추가, 삽입, 삭제, 수정 후 다시 튜플로 변경
tup = (1,2,3,4,5)
# 튜플 -> 리스트
lis = list(tup)
print(tup, type(tup))
print(lis, type(lis))

lis.append(6)

# 리스트 => 튜플
tup = tuple(lis)
print(lis, type(lis))
print(tup, type(tup))
print('*' * 30)

# 삭제 안됨
# tup.remove(3)
# tup.pop(3)
# del tup[2]

# 수정 안됨
# tup[3] = 15