# (0,0), (x,y), (w,h)에서 직사각형 크기는 (w,h)가 결정 짓는다. 그럼 (x,y) 기준으로 직사각형의 모서리에 도달하는 최단 거리를 구하는 문제이다. 
# 내가 봤을땐 x,y기준으로 0,0 뺀 값하고 w, h를 뺀 값하고 비교해서 제일 작은 값을 표현하면 되지 않나 싶다.
N = int(input())
for i in range(9):
    print(str(N) + ' * ' + str(int(i+1)) + ' = ' + str(N * (int(i+1))))
# 생각보다 간단하지 않았다. for의 range를 걸어서 9단까지 반복하도록 설정했다.
# 변수 N이나 여러 값이 정수 형이어서 출력을 하지 못해 str로 형 변환을 해서 출력하도록 했다.