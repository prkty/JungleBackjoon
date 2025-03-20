# 먼저 첫째 줄에는 수의 개수와 둘째 줄은 수가 들어가야하므로 input을 먼저 받는다.
N = int(input())
list_x = []    # 리스트 생성

for i in range(N):   # 인자 i를 N의 갯수만큼 받는다.
    i = int(input())  # 인자 i에 입력
    list_x.append(i)   # x리스트에 입력된 i 추가
    list_x.sort() # sort 함수로 리스트 내용 오름차순 정렬
# (사실상 sort는 for문 밖에 써도된다. 입력 받을 때마다 정렬하나 입력 다 받고 정렬하나 같으니까)
# print(list_x)
# 내가 여기까지 썻는데, 정렬은 되는데, 출력 조건처럼 안나오길래 찾아봤더니 for문으로 N번 돌려서 인자를 하나씩 
# 출력하게끔 해야됐다.

# print(list_x)를 다음과 같이 바꾼다.
for i in range(N):   # 인자 갯수 만큼 만복
    print(list_x[i])  # N번까지 인자 i를 출력한다.
    
# for문으로 list의 인자값을 하나씩 출력시키는 것 외의 코드는 자력으로 짜봤는데
# 쉬운 코드라도 자력으로 풀어보았으니 뿌듯한 감이 있다.