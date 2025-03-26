# 이 문제를 풀기 위해서는 행렬제곱이 어떤 것이고 어떻게 푸는지 알아야한다.
# 행렬 제곱을 어떻게 하는지 기억이 안나서 찾고 다시 왔다.
# 행렬 A에 B를 제곱하는 프로그램을 만든는데, A^B의 각 원소를 1000으로 나눈 나머지를 출력한다.
# 행렬을 빠르게 구하기 위해서는 B가 짝수일시(B % 2 == 0) -> A^B=(A^(B/2))×(A^(B/2))
# B가 홀수일시(B % 2 == 1) -> A^B=(A^((B-1)/2))×(A^((B-1)/2))×A
# 짝수는 그냥 반으로 나누고, 홀수면 반으로 나눈것에 한 번 더 곱해주면된다.
# 라는 특징을 생각하여 재귀적으로 B를 줄이면서 연산하면 빠르게 값을 구할 수 있습니다.
# A를 B만큼 곱하면 느리니, 쪼개서 계산한다고 생각하면 편하다.

import sys

# 1. 입력 받기
N, B = map(int, sys.stdin.readline().split())  # 행렬 크기 N, 거듭제곱 B
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 행렬 입력(2차원배열)

# 2. 행렬 곱셈 함수 (A × B)
def matrix_mult(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]  # 결과 행렬 초기화

    for i in range(size):
        for j in range(size):
            for k in range(size):  # 행렬 곱셈 규칙 적용
                result[i][j] += A[i][k] * B[k][j]   # 2차원 배열로 요소가 2개이다
            result[i][j] %= 1000  # 문제 조건: 모든 원소는 1000으로 나눈 나머지
    return result

# 3. 행렬 거듭제곱 함수 (A^exp)
def matrix_pow(A, exp):
    if exp == 1:  # ✅ A^1 = A
        return [[element % 1000 for element in row] for row in A]  # ✅ 1000으로 나눈 나머지 처리

    half = matrix_pow(A, exp // 2)  # A^(B/2) 계산
    half = matrix_mult(half, half)  # A^(B/2) × A^(B/2)

    return matrix_mult(half, A) if exp % 2 else half  # B가 홀수면 A 한 번 더 곱함

# 4. 결과 계산 및 출력
result = matrix_pow(matrix, B)
for row in result:
    print(*row)  # 행렬 출력
    
# 솔직히 이해가 잘 되지않는다. 애초에 행렬제곱 이론이 쉽지 않다.
# 다 알지 못하지만 해당문제도 시간이 지나 다시 이해해보러 오겠다.

