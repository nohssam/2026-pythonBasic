# set(집합) : 중복을 허용하지 않는다.
#             정해진 순서가 없으므로 인덱싱으로 값을 얻을 수 없다.
#            {항목, 항목, 항목}
# 중복을 허용하지 않는 것 : set과 dict의 key

s1={1,3,5,7,9}
print(s1 ,type(s1))

# 중복을 허용하지 않는다.
s2 = {1,3,5,7,9,2,3,4,5,6,7}  # set
s3 = [1,3,5,7,9,2,3,4,5,6,7]  # list
s4 = (1,3,5,7,9,2,3,4,5,6,7)  # tuple
print(s2)
print(s3)
print(s4)
print('-' * 50)

# set은 인덱싱 못한다.(인덱스가 없다.)
# list나 tuple로 변경하면 인덱싱 가능 ( list(set),  tuple(set)  set(list), set(tuple)
# print(s2[3])
print(s3[3])
print(s4[3])
print('-' * 50)

# 교집합(&), 합집합(|), 차집합(-)
s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

# print(s1+s2) # 오류 (리스트와 튜플은 + 연산 가능)
print(s1 & s2, type(s1&s2))
print(s1 | s2, type(s1|s2))
print(s1 - s2, type(s1-s2))
print(s2 - s1, type(s2-s1))
print('-' * 50)

# 함수 사용
print(s1.intersection(s2), type(s1.intersection(s2))) # 교집합
print(s1.union(s2), type(s1.union(s2)))              # 합집합
print(s1.difference(s2), type(s1.difference(s2)))    # 차집합

s3={1,3,5,7,9}
# 추가 ; add
# s3.append(11)

s3.add(11)
print(s3)

# 삭제 : remove(항목), clear() =>전체삭제
s3.remove(7)
print(s3)

# 없는 항목은 오류
# s3.remove(8)
# print(s3)

# 리스트 + 리스트
lis4 = [1,3,5,7,9]
lis5 = [2,4,6,8,10]
res = lis4 + lis5
print(res)

s4 = {1,3,5,7,9}
s5 = {2,4,6,8,10}
res = s4 | s5
print(res)

s4 = {1,3,5,7,9}
s5 = {2,4,6,8,10}
res = s4.union(s5)

s4 = {1,3,5,7,9}
s5 = {2,4,6,8,10}
s4.update(s5)
print(s4)




