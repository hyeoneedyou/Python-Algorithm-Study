# 이진 탐색(Binary Search)

## 순차 탐색(Sequential search)
- 리스트 안에 있는 트정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 순차 탐색 소스코드
```python
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")  
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

## 이진 탐색(Binary Search)
- 반으로 쪼개면서 탐색하기
- 배열 내부의 데이터가 정렬되어 있어야 사용 가능
- `시작점`,`끝점`,`중간점`
- 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음
- 재귀함수를 이용하는 방법, 반복문 이요하는 방법으로 구현 가능
```python
# 이진 탐색 소스코드 구현 (재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
```python
  
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
```
## 트리 자료구조
- `루트 노드`,`단말 노드`, `서브 트리`
- 데이터를 트리 자료구조로 저장해서 이진탐색과 같은 탐색기법을 이용해 빠르게 탐색 가능

## 이진 탐색 트리
- `왼쪽 자식 노드` < `부모 노드` < `오른쪽 자식 노드`
- 이진 탐색 트리 자료구조를 구현하도록 요구하는 문제는 출제 빈도가 낮으므로 구현되어 있다고 가정하고 데이터를 조회하는 과정만 알면 됨


### 빠르게 입력받기
- 데이터 개수가 1000만개를 넘어가거나 탐색 범위의 크기가 1000억 이상일 때
- `input()`은 시간 초과가 뜰 수 있음
- `sys` 라이브러리의 `readline()`함수를 이용하면 시간초과를 포기할 수 있음
- `rstrip()`을 해줘야 엔터와 같은 공백 문자 제거 가능
```python
import sys

# 하나의 문자열 데이터 입력 받기
input_data = sys.stdin.readline().rstrip()
# 입력 받은 문자열 그대로 출력하기
print(input_data)
```


