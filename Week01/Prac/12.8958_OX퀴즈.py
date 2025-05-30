# 테스트 케이스는 for in range로 설정하고 if문으로 문자열 불러 와서 O와 X를 관계 연산자로 하면 될 것 같다.
# 문제는 연속적으로 숫자를 맞추면 1이 추가된다(1+2+3 ...) 이걸 count를 사용해서 해결하나? ++i 같은 걸로 해결할지 고민이다.
# 문자를 연속적으로 맞추면 1을 카운트해서 올려준다음 더해주고, 만약 x가 나오면 1로 다시 초기화한다.
x = int(input())
    
for i in range(x):
    OX = input() # 기본 인풋이 str이다.
    score = 0
    sum_score = 0  # 각 들여쓰기 할때마다 0으로 초기화한다.
    for i in OX :
        if i == "O":      # O가 나오면 더해줄 값이 1이 추가 된다. 1을 더한값이 score에 다시 할당된다.
            score += 1
        else:
            score = 0     # 그외의 값이면 0으로 초기화한다.
        sum_score += score   # 연속적으로 맞은 만큼 더해진다.
    print(sum_score)
    
# 답이 정상적으로 안나와서 확인해 봤더니 줄바꿈 문제가 있었다. 줄바꿈을 어떻게 하느냐에 따라 값이 달라진다.
# 좀 많이 어려운 문제였다. O 개수만큼 +1씩 더 더해지니 어려웠다. 나중에 한번더 이해해야겠다.