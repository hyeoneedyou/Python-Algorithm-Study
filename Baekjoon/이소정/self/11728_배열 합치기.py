# A배열크기 B배역 크기
# A배열
# B배열

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
new_list = a_list + b_list
print(*sorted(new_list))