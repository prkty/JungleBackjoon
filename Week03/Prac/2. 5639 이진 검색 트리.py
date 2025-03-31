# 이진 트리의 이론은 모든 왼쪽 자식들 <= 부모노드 < 모든 오른쪽 자식들 의 규칙을 치켜야한다.
# 입력은 전위 순회이고 출력은 후위 순회이다.
# 인덱스만 가지고 트리를 구현한다.
# 직접 트리를 구현하면 오류가 나온다.(시간이 오래걸려서)
# 그래서 딕셔너리를 통해서 구현한다.
# 정산적인 출력을 위해 EOF 처리를 해주는데 팀원분들을 통해 좋은 정보를 알았다.
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Node:                 # 노드 설정
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

nodes = []
while True:     # 노드 입력 처리
    try:
        nodes.append(Node(int(input())))
    except:
        break


class Tree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, node):   # 노드 추가
        if self.root is None:   # 아무것도 없으면 입력
            self.root = node
            
        else:     # 자식 노드가 있으면 검사
            root = self.root
            while True:
                
                # 작으면 left
                if node.data < root.data:  # 추가할 노드가 이미 있는 루트보다 작으면
                    if root.left is None:
                        root.left = node
                        break
                    else:
                        root = root.left
                        
                # 크면 right (같은 경우는 없음)
                else:
                    if root.right is None:
                        root.right = node
                        break
                    else:
                        root = root.right
                        
# 후위 순회 진행
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)

# 노드 입력
tree = Tree()
for node in nodes:
    tree.insert(node)

postorder(tree.root)   

# 해당 방식에 대해서 여러 방법을 살펴보았다. 딕셔너리, 리스트로 구현하는 방식이 있지만
# 원리적으로 left, right로 노드를 추가해서 구현해 보고 싶었다. 거의 토요일 하루종일 했지만
# 100퍼센트 이해하지 못했다. 내일 다시한번 보겠다.

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# NUM = []


# while True:      # N을 받아서 입력 횟수를 받지 않기 때문에 공백이 입력되면 종료시키는 EOF처리를 해준다.
#     try:
#         NUM.append(int(input()))
#     except:
#         break


# def post_order(left, right):   # 입력단 전위 순회 구현
#     if left > right:   # 직전값과 현재값 비교해서 직전값이 크면 종료
#         return
#     mid = right + 1     # mid는 오른쪽 서브트리의 시작 인덱스를 저장할 변수
    
#     for i in range(left+1, right+1):  # 현재 서브트리의 범위 내에서 탐색
#         if NUM[left] < NUM[i]:  # 현재 루트보다 큰 값이 나오면 오른쪽 서브트리 시작점
#             mid = i
#             break    # 찾으면 바로 루프 종료

#     # 재귀적으로 왼쪽 오른쪽 서브트리 탐색
#     post_order(left+1, mid-1)   # 왼쪽 서브트리 탐색 (NUM[left]보다 작은 값들)
#     post_order(mid, right)    # 오른쪽 서브트리 탐색 (NUM[left]보다 큰 값들)
    
#     # 루트 출력
#     print(NUM[left])    # 현재 서브트리의 루트 노드 출력

# # 후위 순회
# post_order(0, len(NUM)-1)