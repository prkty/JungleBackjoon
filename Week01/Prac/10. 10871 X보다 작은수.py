# N과 X를 먼저 받아야한다. 출력은 list를 입력 받은 수중 X보다 작은 수를 출력하게끔 해야한다.
N, X = map(int, input().split())
a = list(map(int,input().split())) 
# list의 여러값 인풋 받는 것도 map을 사용하여 자료형을 int로 전환해서 한 줄로 넣을 수 있다.

for i in range(N):
    if a[i] < X:
        print(a[i], end = " ")   # 요소 사이에 공백을 추가하기 위해 end를 사용한다.
# 리스트 요소를 꺼내서 비교를 해서 작으면 뽑아 내는 것을 어케하는지 몰랐다.
# 문제의 핵심인 리스트에 있는 값을 자연수와 비교하려면 for문과 if문을 쓴다. 
# 정수 N개라는 제한을 걸어야하므로 for의 range(N)으로 범위를 제한하고, if로 X와 비교해 작은 리스트의 요소만 출력되게 한다.