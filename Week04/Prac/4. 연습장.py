import sys
input = sys.stdin.readline

A = input().strip()
n = len(A)
B = input().strip()
m = len(B)

LCS = [[0]* (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 1+m):
        if i == 0 or j == 0:  # 마진 설정
            LCS[i][j] = 0
        elif A[i] == B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
            
print(LCS[i][j])