import sys

card_num = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))
card_list.sort()

is_card_list = []
q_num = int(sys.stdin.readline())
q_list = list(map(int, sys.stdin.readline().split()))

for q in q_list:
  left = 0
  right = card_num
  mid = (left + right)//2
  is_card = False
  while left < right:
    mid = (left + right)//2
    if card_list[mid] < q:
      left = mid + 1
    elif card_list[mid] > q:
      right = mid
    else:
      is_card = True
      break
  if is_card:
    is_card_list.append("1")
  else:
    is_card_list.append("0")

answer = " ".join(is_card_list)
print(answer)
