# str으로 문자열을 받고 그걸 split 공백으로 나눈 갯수를 세면 되지 않을까 싶다.
x = input().split()
print(len(x))  # 요소의 갯수는 len을 쓴다!!

# 더욱 간단히 나타내면 다음과 같다.
print(len(input().split()))
