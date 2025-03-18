# 문제에서 고려할 사항을 살펴보았다.
# 길이가 짧은 순이며 길이가 같을 시 사전순이어야한다. 중복 단어는 제거해야한다.
# 첫째 줄엔 단어의 개수 N을 센다.
import sys

N = int(input()) 
list_word = []   # 단어 들어갈 리스트를 만든다.


for i in range(N):
    i = str(sys.stdin.readline().strip())  # 인풋대신 readline으로 빠르게 받는다. 
    # 이렇게하면 개행 문자 \n을 같이 보여주므로 strip을 통해 제거해준다.
    list_word.append(i)    # 알파벳 리스트에 저장
    
setting_word = set(list_word)   # 리스트의 값중 중복값을 set 함수로 없앤다.
list_word = list(setting_word)    # set으로 인해 리스트가 풀렸으므로 다시 리스트화 시킨다.
list_word = sorted(list_word)   # 리스트의 값을 알파벳순으로 정렬한다. (둘째 조건)
list_word = sorted(list_word, key = len)   # 리스트의 값을 길이 순으로 재정렬한다. (첫 조건)
# key를 통해 정렬기준 길이로(len) 조정 가능
# 조건 우선 순위가 높은 걸 밑에 적어야한다. 코드는 순차적으로 처리하므로

for i in list_word:    # 리스트에 있는 요소(알파벳)들을 한 줄씩 출력, 범위가 따로 필요없어 간단히 출력된다.
    print(i)
    
# 전과 달라 살짝 당황했지만, set으로 중복값을 없앨수 있고 list로 다시 묶어줘야한다는 것을 알았다.
# 조건의 우선순위가 높은 것을 나중에 수행해야하고, key = len 을 통해 길이 순으로 리스트를 정렬할 수 있다는 사실을 깨달았다.
# 전과 달리 정해진 N회차 만큼 리스트 요소를 프린트 안해도 간단하게 바로 출력하는 방법도 알게 되었다.(간편한 방법이 있었구나...)