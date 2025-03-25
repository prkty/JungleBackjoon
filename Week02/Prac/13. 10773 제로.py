# 일단 재현이는 잘못된 수를 부르면 0을 통해 최근 수를 지운다.(pop)
# 모두 적고 난 이후의 수들의 합을 알고 싶다.(sum)
K = int(input())
stack = []

for _ in range(K):
    cmd = input()
    
    if cmd == "0":
        stack.pop()     # 0일시 하나 뽑아낸다.
    else:
        stack.append(int(cmd))   # 그외의 경우 입력된 값을 넣는다.
        
print(sum(stack))

# 자력으로 풀었다. 간단하지만, 뭔가 뿌듯하다.