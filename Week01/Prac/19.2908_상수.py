# 파이썬에는 reversed라는 요소를 뒤집을 수 있는 함수가 있다. 이 함수를 사용해 요소를 뒤집은 다음에
# 두 개의 요소를 비교하여 max로 큰 수를 뽑으면 될 것 같다.
x, y = list(input().split())
reverse_x = reversed(x)  # reversed를 통해 뒤집어진 리스트의 값을 받는다.
reverse_y = reversed(y) # reverse는 리스트를 뒤집고 리턴 값이 없어 non이 나온다.
print(max(''.join(list(reverse_x)), ''.join(list(reverse_y)))) 
# reversed는 뒤집어진 리스트의 값을 리턴하므로 list로 묶어줘야 일반적인 값이 나온다. 
# 뒤집어진 각각의 숫자를 join을 통해 합친다음에 max로 둘중 큰 수를 출력한다.

# 여기서 reverse와 reversed의 차이가 헷갈리는데, 
# reverse는 리턴값이 없어서 그 자체로 표현이 된다. 함수의 값으로 쓰기 힘들다.
# 그러나 reversed는 뒤집어진 리스트 값의 리턴값을 주기 때문에 함수에 list와 함께 저장해줄 수 있다. 