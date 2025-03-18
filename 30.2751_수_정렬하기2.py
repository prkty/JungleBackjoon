# 기존의 2750 코드를 사용하면, 범위가 커서 시간 초과가 나온다.
# 그래서 조사를 해봤더니, input 대신 파이썬의 sys.stdin.readline()를 사용해서 처리해야한다.
# 왜냐히면, input으로 받으면 prompt message로 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다고 한다.
# 그러나 sys.stdin.readline()은 input과 반대이므로 개행 문자를 포함한다는 점 뺴고는 빠르다는 장점이 있다.
import sys   # sys.stdin.readline()를 쓰기 위해 임포트 해준다.

N = int(input())
list_x = []    # 리스트 생성

for i in range(N):   # 인자 i를 N의 갯수만큼 받는다.
    i = int(sys.stdin.readline())  ### sys.stdin.readline()를 input 대신 써준다.
    # sys.stdin.readline()을 쓸때 주의 점은 기본타입이 str의 개행 문자라 \n과 같이 저장되므로 int로 형변환해서 써야된다. 
    list_x.append(i)   # x리스트에 입력된 i 추가
list_x.sort() # sort 함수로 리스트 내용 오름차순 정렬

for i in range(N):   # 인자 갯수 만큼 만복
    print(list_x[i])  # N번까지 인자 i를 출력한다.
