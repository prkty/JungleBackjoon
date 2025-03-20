N = input()  # 각각의 숫자를 분리해서 받기 위해 string 변환

if len(N) == 1:   # 초기에 일의 자리일 경우 대비
    N = "0" + N  # 한 자리 숫자는 앞에 0을 붙여서 두 자리로 맞춤
        
old_N = N   # 과정을 통과한 출력값이 처음 값이랑 같을시
count = 0   # 카운트는 0으로 초기화

while True:
    add = str(int(N[0])+int(N[1]))   # add는 더해진 결과값
    
    if len(add) == 1:   # 만약 주어진 수가 10보다 작다면
        add = "0" + add  # 한 자리 숫자일 경우 앞에 0 추가

    N = N[1] + add[1]  # 새로운 숫자 생성
    count += 1 # 시도할 때마다 카운트하는 함수에 +1을 한다.
    
    if N == old_N:
        break
print(count)

