# 나는 조건문 if문을 통해 입력값을 특정 범위에 따라 정해진 출력값을 출력하도록 구상했다.
# 값 제한은 관계연산자로 하고 if문을 조금 이나마 줄이기 위해 or 논리 연산자를 사용헀다.
A = int(input())

if 100 <= A or A >= 90 :
    print('A')
elif 89 <= A or A >= 80 :
    print('B')
elif 79 <= A or A >= 70 :
    print('C')
elif 69 <= A or A >= 60 :
    print('D')
else:
    print('F')