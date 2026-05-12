# 문자열(str): 큰 따옴표, 작은 따옴표 모두 사용 가능
# 여러줄 일때는  ''' 내용 ''',  """ 내용 """
# 주요 연산자 :  +(연결), *(반복), in(포함여부), not in(미포함 여부)

str = '헬로 python'
print(str, type(str))

str = "헬로 python"
print(str, type(str))

str = "I'm Ok !!"
print(str, type(str))

str = 'I"m Ok !!'
print(str, type(str))

# 이스케이프 문자(리터럴 문자) : \n(줄바꿈),  \t(탭), \"("), \'(')
# {'name' : 'hong'}
str = "{\'name\' : \'hong\'}"
print(str, type(str))

str = "{'name' : 'hong'}"
print(str, type(str))

str = "@"
print(str + str)  # @ + @ = @@

print(str * 5)    # @ * 5 = @@@@@


str = "Hello"
# in : 포함 되면 True
print("H" in str)     # True
print("llo" in str)   # True
print("hello" in str) # False

# not in : 포함되지 않으면 True
print("x" not in str)      # True
print("Hello" not in str)  # False