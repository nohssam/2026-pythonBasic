# dict(딕셔너리) : key, value 로 이루어져 있음

dic = {'name':'hong', 'age':24, 'gender': True}
print(dic, type(dic))

dic2 = {101:'hong', 102:24, 103: True}
print(dic2, type(dic2))
print('*' * 50)

# key를 이용해서 value을 호출
print(dic["name"], type(dic["name"]))
print(dic2[102] , type(dic2[102]))

# key만 얻기
print(dic.keys() , type(dic.keys()))

# value만 얻기
print(dic.values() , type(dic.values()))
print('*' * 50)

# 편하게 사용하기 위해서는 dict_keys, dict_values 를 리스트로 변경할 수 있다.
lis1 = list(dic.keys())
print(lis1)

lis2 = list(dic.values())
print(lis2)
print('*' * 50)

dic = {'name':'hong', 'age':24, 'gender': True}

# 값 가져오기 : items()
print(dic.items() , type(dic.items()))
# dict_items([('name', 'hong'), ('age', 24), ('gender', True)]) <class 'dict_items'>

# [('name', 'hong'), ('age', 24), ('gender', True)] <class 'list'>
print(list(dic.items()), type(list(dic.items())))

# ('name', 'hong')
print(list(dic.items())[0])

print(list(dic.items())[0][0]) # name
print(list(dic.items())[0][1]) # hong
print("-"*50)

# 값 가져오기 :get(key)
dic = {'name':'kang', 'age':10, 'gender': True}
print(dic.get('name'))
print(dic["name"])

# 없는 key를 넣으면 None
print(dic.get("hobby"))  # None
# print(dic["hobby"])     # 오류 발생
print("-"*50)

# in 사용가능
# 해당 key가 dict 안에 있는지 검사 : in
print('name' in dic)  # dic안에 name 키가 있으면 True, 없으면 False
print('hobby' in dic) # dic안에 hobby 키가 있으면 True, 없으면 False
print("-"*50)

# 데이터 수정
dic = {'name':'kang', 'age':10, 'gender': True}
dic["name"] = "Kim"
print(dic)
print("-"*50)

# key는 중복 안됨
dic = {'name':'kang', 'name':'Park',  'age':10, 'gender': True}
print(dic)