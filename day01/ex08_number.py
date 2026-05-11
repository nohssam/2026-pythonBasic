# 비교연산자 (결과는 항상 True/False)
# 논리연산자 (결과는 항상 True/False)
from xmlrpc.client import Fault

su1 = 7
su2 = 3

print(f"{su1 > su2 = }")
print(f"{su1 >= su2 = }")
print(f"{su1 < su2 = }")
print(f"{su1 <= su2 = }")
print(f"{su1 == su2 = }")
print(f"{su1 != su2 = }")

# 논리연산자 (and, or, not)
print(f"{True and True = }")   # True
print(f"{True and False = }")  # False
print(f"{False and True = }")  # False
print(f"{False and False = }") # False
print()

print(f"{True or True = }")    # True
print(f"{True or False = }")   # True
print(f"{False or True = }")   # True
print(f"{False or False = }")  # False

age = 17
print(f"{bool(age)=}") # True

print(f"{not bool(age)=}") # False
print(f"{not age = }")     # False