# list  연산
# + (합치기) , * (반복)
# in, not in


su1 = [1,2,3]
su2 = [4,5,6]

print(su1 + su2)  #[1, 2, 3, 4, 5, 6]
print(su2 + su1)  #[4, 5, 6, 1, 2, 3]

print(su1 * 3)    # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print('-' * 30)

# 안되는 연산
# print(su1 - [1]) : 빼기 불가
# print(su1 * su1) :  리스트 * 리스트 불가
# print(su1 + 1)  : 리스트 + 숫자 불가

su1 = [1,2,3]
print(1 in su1)  # True
print(5 in su1)  # False
print('-' * 30)

print(1 not in su1) # False
print(5 not in su1) # True