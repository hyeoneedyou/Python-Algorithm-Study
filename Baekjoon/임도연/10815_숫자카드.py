# 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
# 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
# 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
s = int(input())  # 숫자카드 수
s_card = list(map(int, input().split()))  # 상근이 숫자카드
s_card.sort()
m = input()  # 주어질 숫자카드 수
cards = list(map(int, input().split()))  # 주어진 숫자카드


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


result = []
for card in cards:
    a = binary_search(s_card, card, 0, s - 1)
    if a is None:
        result.append("0")
    else:
        result.append("1")
print(' '.join(result))
