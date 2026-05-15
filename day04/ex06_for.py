#  60점 이상 이면 합격

# 리스트
t_list = [90,25,67,45,80,75]
success = []
fail = []
for i in t_list:
    if i >= 60:
        success.append(i)
    else:
        fail.append(i)

print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")

success = [i for i in t_list if i >= 60]
fail = [i for i in t_list if i < 60]
print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")
print('-' * 50)

# set
t_set = {90,25,67,45,80,75}
success = set()
fail = set()

for i in t_set:
    if i >= 60:
       # success.append(i)
       success.add(i)
    else:
       # fail.append(i)
      fail.add(i)
print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")

success = {i for i in t_set if i >= 60}
fail = {i for i in t_set if i < 60}
print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")
print('-' * 50)

# dict
t_dict = {
    "둘리" : 90,
    "일지매": 25,
    "장길산": 67,
    "홍길동" : 45,
    "전우치" : 80,
    "임꺽정" : 75
}
success = {}
fail = {}

for name, score in t_dict.items():
    if score >= 60:
        success[name] = score
    else:
        fail[name] = score
print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")

success = { name:score for name, score in t_dict.items() if score >= 60 }
fail = { name:score for name, score in t_dict.items() if score < 60 }
print(f"합격자 {len(success)}명 : {success}")
print(f"불합격자 {len(fail)}명 : {fail}")