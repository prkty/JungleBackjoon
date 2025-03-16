# 일단 3자리를 받을 수 있는 인풋을 받고 곱한다. 그럼 값이 나올 것인데
# 나온 값을 쪼개서 리스트화한다.(len쓰면 될 것 같다)
# 리스트에서 0~9까지 추출해서 갯수를 센다.
A = int(input())
B = int(input())
C = int(input())
ABC = A * B * C

x = []
for i in str(ABC):
    x.append(i)
    
# cnt0 = x.count("0")
# print(cnt0)
# cnt1 = x.count("1")
# print(cnt1)
# cnt2 = x.count("2")
# print(cnt2)
# cnt3 = x.count("3")
# print(cnt3)
# cnt4 = x.count("4")
# print(cnt4)
# cnt5 = x.count("5")
# print(cnt5)
# cnt6 = x.count("6")
# print(cnt6)
# cnt7 = x.count("7")
# print(cnt7)
# cnt8 = x.count("8")
# print(cnt8)
# cnt9 = x.count("9")
# print(cnt9)

# 너무 단순 무식하게 써서 for문으로 바꿀 방법을 찾고 있다.
# for문은 1부터 9까지 반복하는데, 그걸 str형식이랑 비교해서 추출할 수 있는지 모르곘다.

for i in range(10):
    print(x.count(str(i)))
    
# 단순화하는 방법은 GPT한테 물어보았다. 반복하는 i를 str으로 변환해서 카운트하면 되는 간단한 문제였다... 