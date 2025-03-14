A,B = map(int, input().split())  #map을 통해 같은 줄에 입력 값을 줄수 있다. map(function, iterable)을 통해 펑션은 각 요소에 적용할 함수, 인터에이블은 함수를 적용할 데이터 집합이다. 
#인풋을 받아 공백만큼 split 한 후 map함수를 통해 int를 바꿔준다.

print(A+B)
print(A-B)
print(A*B)
print(A//B)  #몫만 구할 시 //로 구한다. /는 일반적인 나눗셈으로 소수점까지 나온다.
print(A%B)