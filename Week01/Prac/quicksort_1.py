from typing import MutableSequence

global call_count
call_count = 0

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬 (내림차순)"""
    global call_count
    call_count += 1  # 재귀 호출 횟수 증가
    
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:
        while a[pl] > x: pl += 1   # 내림차순: 큰 값 찾을 때까지 이동
        while a[pr] < x: pr -= 1   # 내림차순: 작은 값 찾을 때까지 이동
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬 (내림차순)"""
    global call_count
    call_count = 0  # 호출 횟수 초기화
    qsort(a, 0, len(a) - 1)
    print(f'퀵 정렬 재귀 호출 횟수: {call_count}')

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다. (내림차순)')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('내림차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
