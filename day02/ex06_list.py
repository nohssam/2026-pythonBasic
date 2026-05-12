# list는 추가 , 삽입 , 삭제, 수정 모두 가능 (가변형)
su1 = ["사과", "배", "포도"]

# 추가 : append
su1.append("바나나")
print(su1)

# 삽입 : insert(index, 데이터)
su1.insert(2, "망고")
print(su1)

# 수정 : list[index] = 데이터
print(su1[1])
su1[1] = '수박'
print(su1)

# 데이터 삭제 : remove, pop, del
# remove : 만약 수박이 여러개 있으면 첫번째만 삭제
su1.remove("수박")
print(su1)

# 없는 데이터 삭제하면 오류 발생
# su1.remove("메론")

# pop : 인덱스로 삭제 , 삭제된 데이터 반환
#       인덱스를 생략하면 마지막 데이터 삭제
res = su1.pop(2)
print(f"{res=}")
print(f"{su1=}")
print("-" * 30)

#인덱스를 생략하면 마지막 데이터 삭제
res = su1.pop()
print(f"{res=}")
print(f"{su1=}")
print("-" * 30)

# del- 인덱스 또는 슬라이싱으로 삭제

su1 = [1,2,3,4,5]
del su1[0]
print(su1)

del su1[1:]
print(su1)

# 변수 자체 삭제
del su1
# print(su1)

