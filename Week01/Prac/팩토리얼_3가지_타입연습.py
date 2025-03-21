# 재귀함수
def factorial (n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
    

n = int(input())
print(factorial(n))

    
# for문
n = int(input())
result = 1
for item in range(n, n+1, 1):  
    result *= item
print(n)
# for문은 재귀함수와 다르게 1부터 n까지 올라가면서 곱한다.


# math 라이브러리 사용
import math
n = int(input())
print(math.factorial(n))