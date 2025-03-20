T = int(input())


for _ in range(T):  # 입력된 T까ㅈ지 반복
    n = int(input())
    SUM = 4
    더하기 = [None,1,2,4]  # 케이스별로 초기화
    
    while SUM <= n:   # 총합이 4보다 작을 때까지 계속함
        더하기.append(더하기[SUM - 1] + 더하기[SUM -2] + 더하기[SUM-3])
        SUM += 1
        
    print(더하기[n])
    