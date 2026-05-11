# 숫자형(Number)
# 정수(int),  실수(float), 복소수(complex), 지수

# 1. 정수
age = 18
print(f"{age=}, type={type(age)}")

# 2. 실수
weight = 72.14
print(f"{weight=}, type={type(weight)}")

#3. 복소수(실수, 허수)
num = 415 + 34j
print(f"{num=}, type={type(num)}")

# 실수부분
print(f"{num.real=}, type={type(num.real)}")

# 허수부분
print(f"{num.imag=}, type={type(num.imag)}")

# 4. 지수 표현
height = 1.817e2 #(1.817 * 10^2 ) = 181.7
print(f"{height=}, type={type(height)}")

height = 1.817e5 #(1.817 * 10^5 ) = 181700
print(f"{height=: ,}, type={type(height)}")

# 5. 8진수(0o숫자) : 0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,20
num1 = 0o11
print(f"{num1=}, type={type(num1)}")

# 6. 16진수(0x숫자):0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,10,11,12,13,14,15,16,17,18,19,1a,1b,1c,1d,1e,1f,20
num2=0x11
print(f"{num2=}, type={type(num2)}")