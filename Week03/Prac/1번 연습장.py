import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
tree = {}

for i in range(n):
    root, left, right = map(str, input().split())
    tree[root] = left, right
    print(tree)
    
def pre(v):
    if v != ".":
        print(v, end="")
        pre(tree[v][0])
        pre(tree[v][1])
        
def mid(v):
    if v != ".":
        mid(tree[v][0])
        print(v, end="")
        mid(tree[v][1])
        
def post(v):
    if v != ".":
        post(tree[v][0])
        post(tree[v][1])
        print(v, end="")
        
pre('A')
print()
mid('A')
print()
post('A')