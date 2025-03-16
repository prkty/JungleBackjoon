# sum(a)를 쓰면 합을 구한다. 파이썬에서는 타입 힌트를 줄 수 있다고 한다.
# 리스트 형을 int 형으로 내보내야하니, 다음과 같이 써서 리스트인 a를 리턴으로 int형이 온다고 타입 힌트를 주면 된다.
def solve(a: list) -> int:
    return sum(a)

# 문제엔 형태가 정해져 있어서 이렇게 썻지만 간단하게 쓸수 있다.
def solve(a):
    return sum(a)