# 팩토리얼은 for문을 통해 구현가능할 것 같다.
# 인풋 받은 N 값을 1부터 차례로 1씩 올리며 곱하면서 N 값까지 구하면 된다.
N = int(input())
F = 1

for i in range(1, N+1):  # 1부터 N까지 모든 요소(i)를 곱합니다.
    F *= i
    
print(F)

# 책이나 인터넷 자료를 찾아보니 팩토리얼을 구하는 방식이 다양하다.
# 본인을 다시 호출하는 재귀함수를 사용한 방법도 있다.
def factorial(n):
   if n > 1:
       return n * factorial(n-1)
   else:
       return 1 
   
n = int(input())  # 입력 받기
print(factorial(n))  # 팩토리얼 계산 후 출력