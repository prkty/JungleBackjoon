# 먼저 N개의 정수를 입력받아야한다. 비교할 줄인 다음줄 M개의 정수도 입력 받아야한다.
# 힌트가 이진 검색트리이니, 해당 방식으로 구현해 보겠다. 이진 검색트리는 이진검색 알고리즘하고 비슷하다.
# 책에 있는 내용을 따왔다.
# 내가 초반에 이진 검색 트리를 써서 시간좀 썻다
# 이진 탐색을 사용하기 위해서는 값이 정렬되어 있어야한다.

from typing import Any, Sequence

def bin_search(num: Sequence, key: Any) -> int:
    pl = 0           # 검색범위 맨 앞 원소의 인덱스
    pr = len(num) - 1  # 검색범위 맨 끝 원소의 인덱스
    
    while pl <= pr:      # pl은 pr보다 작거나 같을 동안
        # pc가 key하고 일치 할 경우에는 pl < pr인 케이스로 if문을 통과해 종료된다.
        # 그러나 key가 일치 하지 않을 때, pl=pr이다. 만약 while True이면 if절로 pl이 pr을 뛰어 넘을때 종료
        # 한다는 조건을 걸고 while문을 한바퀴 더 돌아야하지만, pl과 pr이 일치할때 첫 if문에 만족하지 않는다는 것은
        # 탐색 리스트에서 key값이 없음을 의미하므로 바로 return -1을 출력하면 된다.
        pc = (pl + pr) // 2 # 중앙 지정
        if num[pc] == key:    # 키랑 pc랑 같으면 찾음
            return pc         # pc값을 리턴
        
        elif num[pc] < key:   # 키값이 크면
            pl = pc + 1       # 오른쪽 범위로 이동
            
        else:
            pr = pc - 1       # 키 값이 작으면 왼쪽 범위로 이동
        
    return -1  # 종료(결과에 없음)
    
n = int(input())
num = sorted(list(map(int,input().split())))  # 이진 탐색을 위한 정렬(기준이 될 리스트이므로)
m = int(input())
keys = list(map(int,input().split())) # 찾아야되는 key들

# 이진 탐색 수행 및 결과 출력
for key in keys:   # 한 개씩 돌아가면서 비교
    result = bin_search(num, key)   # 입력 받은 값을 대입
    print(1 if result != -1 else 0)  # 위 함수의 리턴이 -1이 아니면 1 출력