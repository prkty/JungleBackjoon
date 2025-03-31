import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정 (트리가 깊어질 경우 대비)
input = sys.stdin.read

while True:
    try:# 입력 처리 (EOF까지 한 번에 읽기)
        preorder = list(map(int, input()))  # 공백 단위로 정수 리스트로 변환
    except:
        break


# 노드 클래스 정의
class Node:
    def __init__(self, value):
        self.value = value  # 노드의 값
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

# BST 삽입 함수
def insert(node, value):
    if value < node.value:  # 왼쪽 서브트리로 가야 하는 경우
        if node.left is None:
            node.left = Node(value)  # 왼쪽 자식이 없으면 새로운 노드 추가
        else:
            insert(node.left, value)  # 왼쪽 자식이 있으면 재귀적으로 삽입
            
    else:  # 오른쪽 서브트리로 가야 하는 경우
        if node.right is None:
            node.right = Node(value)  # 오른쪽 자식이 없으면 새로운 노드 추가
        else:
            insert(node.right, value)  # 오른쪽 자식이 있으면 재귀적으로 삽입

# 후위 순회 (Postorder Traversal) 함수
def postorder(node):
    if node is not None:
        postorder(node.left)  # 왼쪽 서브트리 탐색
        postorder(node.right)  # 오른쪽 서브트리 탐색
        print(node.value)  # 루트 출력

# 트리 만들기 & 후위 순회 실행
root = Node(preorder[0])  # 첫 번째 값을 루트 노드로 설정
for num in preorder[1:]:  
    insert(root, num)  # 나머지 값들 트리에 삽입

postorder(root)  # 후위 순회 실행



# while True:      # N을 받아서 입력 횟수를 받지 않기 때문에 공백이 입력되면 종료시키는 EOF처리를 해준다.
#     temp = sys.stdin.read()
#     if temp == "":
#         break
