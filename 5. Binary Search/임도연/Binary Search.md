# 이진 탐색

## 순차 탐색
**순차 탐색** : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
```python
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))
```
시간 복잡도 : O(N)

## 이진 탐색
**이진 탐색** : 배열 내부의 데이터가 정렬되어 있을 때, 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 방법

```python
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


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
시간 복잡도 : O(logN)

## 빠른 입력 sys
```python
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
```

## [문제] 부품찾기
> 전자매장에 부품이 N개 있고 각 부품은 정수 형태의 고유한 번호가 있다.
> 손님이 M개 종류의 부품을 대량 구매한다고 할 때, 모든 부품이 있는지 확인하는 프로그램을 작성하라.

```python
# 내 풀이
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
```
-> 집합 자료형을 이용했으나 이진탐색을 이용해 효과적으로 처리할 수 있다.

## [문제] 떡볶이 떡 만들기
> 높이 h를 지정하면 줄지어진 떡을 한번에 절단한다.
> 손님은 잘린 떡의 길이만큼 가져간다.
> 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라.

```python
# 교재 풀이
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)
```
-> 탐색 범위가 매우 크기 때문에 이진탐색으로 구현해야 시간초과가 발생하지 않는다.