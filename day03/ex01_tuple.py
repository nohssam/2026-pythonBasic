# 튜플은 불변(수정 안됨)

# 인덱싱과 슬라이싱
# 인덱싱 : 결과는 각각의 자료형
t1 = (1, 2, 'a', 'b')
print(t1[0], type(t1[0]))
print(t1[2], type(t1[2]))

# 슬라이싱 : 결과는 tuple
print(t1[:2], type(t1[:2]))
print(t1[1:], type(t1[1:]))
print(t1[1:3], type(t1[1:3]))

# 추가 : + 연산을 이용해서 가능
t2 = (1,3,5)
# t2 = t2 + (7) 에서 (7) 는 int 라서 TypeError
t2 = t2 + (7,) # 튜플 + 튜플 가능
print(t2, type(t2))

t2 = t2 + (9,11) # 튜플 + 튜플 가능
print(t2, type(t2))
print('-' * 30)

# 추가 안됨
t3 = (1,3,5,7,9)
# t3.append(11)
# print(t3)

# 삽입 안됨
# t3.insert(2,11)
# print(t3)

# 수정 안됨
# t3[1] = 101
# print(t3)

# 삭제 안됨
# t3.remove(3)
# print(t3)

# 삭제 안됨
# t3.pop()
# print(t3)

# 변수 삭제는 가능
del t3
print('-' * 30)

# 튜플을 추가, 삽입, 수정 하려면
# 리스트로 변경 추가, 삽입, 수정 하고 튜플로 변경
t4 = (1,3,5)

# 튜플 -> 리스트
lis = list(t4)
print(lis, type(lis))

lis.append(7)
print(lis, type(lis))

lis.append(7)
print(lis, type(lis))

lis.insert(1, 10)
print(lis, type(lis))

# 다시 리스트 -> 튜플
t5 = tuple(lis)
print(t5, type(t5))







