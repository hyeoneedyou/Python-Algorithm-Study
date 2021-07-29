# 전자매장에 부품이 N개 있고 각 부품은 정수 형태의 고유한 번호가 있다.
# 손님이 M개 종류의 부품을 대량 구매한다고 할 때, 모든 부품이 있는지 확인하는 프로그램을 작성하라.

import sys

storage = sys.stdin.readline().rstrip()
s_list = list(map(int, sys.stdin.readline().rstrip().split()))
client = sys.stdin.readline().rstrip()
c_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in c_list:
    if i not in s_list:
        print("no", end=" ")
    else:
        print("yes", end=" ")