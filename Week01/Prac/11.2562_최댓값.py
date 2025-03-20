# 9개의 다른 수를 받고 max를 사용한 다음에 몇 번째 수인지 출력하면 되겠다.
listmax=[]
for i in range(9):
    listmax.append(int(input()))  # 여기까지 리스트를 만들고 append를 통해 입력 받은 값을 리스트에 추가한다.
    # 여기 int를 빠뜨리면 틀린다.

print(max(listmax))
print(listmax.index(max(listmax))+1)  # 인덱스를 통해 리스트에서 원하는 값이 몇번째 수인지 출력 가능하다.

# 이렇게 하면 답은 제대로 나오는데, 틀렸다고 해서 찾아봤더니 리스트 인풋 받는 입력값이 자연수여서 int로 받아야한다고 한다. 