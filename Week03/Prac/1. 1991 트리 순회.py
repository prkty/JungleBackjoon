# 파이썬에서 이진 탐색 트리를 만들기 위해 Node와 트리 클래스를 만들어서 설계한다.
# 동료(룸메이트)분께서 알려주셨다. 딕셔너리와 재귀를 통해 루트, 왼쪽, 오른쪽 노드로 나누어서 프린트한다.
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 재귀함수 리미트하여 메모리 초과 방지

n = int(input())
# 딕셔너리로 트리 구현
tree = {}
for i in range(n):
    root, left, right = map(str, input().split())  # 루트, 왼쪽자식, 오른쪽 자식
    tree[root] = left, right  # {'A': ('B', 'C')} 
    # 즉, 입력받은 left, right를 root A의 자식 B,C로 저장한다


def preorder(v):  # 전위순회
    if v != ".":  # 루트 노트가 .이 아니면 (자식이 있다면)
        print(v, end="") # 루트를 우선적으로 출력
        preorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색


def inorder(v):  # 중위순회
    if v != ".":  # .이 아니면
        inorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        print(v, end="")  # 루트 출력
        inorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색


def postorder(v):  # 후위순회
    if v != ".":  # .이 아니면s
        postorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색
        print(v, end="")  # 루트 출력

#루트노드이므로 'A'로 고정
preorder('A')
print()
inorder('A')
print()
postorder('A')

# 어떻게 그전으로 돌아가서 다른 브런치를 찾을까? 재귀함수가 자동으로 스택을 사용하기 때문에 가능하다고 한다.
# 재귀를 호출하면 시스템 스택에 쌓이고 재귀가 끝나면 이전 상태로 복귀한다.
# 그러므로 한쪽 브런치가 완료되면 초기로 돌아가 다음 브런치를 찾는다.