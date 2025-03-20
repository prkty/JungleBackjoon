# 먼저 전체 가로세로값, 몇번 자를지, 자르는 방향과 위치를 인풋으로 받아야한다.
# 3번째 줄부터는 첫 요소는 0이면 가로 1이면 세로이다.
# 대략적인 흐름은 알겠다. 그런데 중간에 자른 선과 자른 선 사이의 길이는 어떻게 구해야하는지 모르겠다.
x, y = map(int,input().split())  # 전체 종이 크기를 지정합니다.
cut = int(input())   # 첫 째줄 전체 길이, 자르는 횟수를 받습니다.

width_cuts = [0, x]   # 가로 방향 점선
height_cuts = [0, y]   # 세로 방향 점선

for _ in range(cut):   # 자른 횟수 만큼 반복
    arrow, position = map(int, input().split())  # 0과 1로 가로인지 세로인지 판단
    # 여기서 주의해야되는 것이 있는데, 0이 가로고 1이 세로이지만 
    # 세로로 자르는 선은 가로에 영향을 주고, 가로로 자르는 선은 세로에 영향을 준다.
    # 이점을 유의해서 설계해야한다. 그림을 그리면 이해하기 편하다.
    if arrow == 1:  # 세로선일시 가로에 영향을 준다. 
        width_cuts.append(position)
    if arrow == 0:  # 가로선일시 세로에 영향을 준다.
        height_cuts.append(position)


# 이제 여기서 받은 요소들을 오름차순으로 정리해서 그 차이중 제일 큰 값 추출해서 곱하기.
width_cuts.sort()
height_cuts.sort()

# 이제 리스트의 앞뒤 값의 차이를 구해야하는데, 어떻게 해야할지 몰라서 GPT의 도움을 받았다.
# GPT는 zip이라는 리스트안에서 세트를 묶을수 있는 새로운 함수를 소개해줬다.
max_width_cuts = max(b - a for a,b in zip(width_cuts,width_cuts[1:])) # 넓이 리스트의 있는 값의 앞뒤 값을 빼서 차이가 제일 큰 것을 추출한다.
max_height_cuts = max(b - a for a,b in zip(height_cuts,height_cuts[1:]))

print(max_height_cuts * max_width_cuts)    