# 평균 구해서 평균을 넘는 학생의 비율을 계산하는 것이 주 핵심이다.
# 근데 두번째 줄부터 앞에 학생 수가 추가 되서 어떻게 입력을 받아야하는지 막막하다.
C = int(input())
    
for _ in range(C):  #for문에서 _를 사용하면 변수가 필요 없이 밑에 과정을 반복한다.
    data = list(map(int, input().split()))  # 한 줄 입력받고 리스트 변환
    N = data[0]  # 첫 번째 값은 학생 수이므로 data 리스트 첫값을 N으로 뺀다
    scores = data[1:]  # 나머지 값을 학생들의 점수로 받는다.
    
    avg = sum(scores) / N  # 평균값 구하기
    avg_up_sum = sum(1 for score in scores if avg < score)
    # 이부분이 좀 어렵다. 먼저 for score in scores로 scores의 내부 요소를 score로 불러온다.
    # 그 후 1 for ~ 에 따라 평균과 비교를 해서 크면 1을 더한다.
    # 결론적으로 평균보다 높은 갯수가 avg_up_sum이 된다.
    print("%0.3f%%"% ((avg_up_sum / N)*100)) 
    # 백분율이므로 100을 곱해주고 %0.3f%% 를 통해 소수 3번쨰 짜리까지 백분율을 추출한다.