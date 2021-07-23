# 정렬
**정렬** : 데이터를 특정한 기준에 따라서 순서대로 나열

## 선택정렬
**선택정렬** : 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 과정을 반복하는 정렬
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```
시간 복잡도 : O(N^2)

## 삽입정렬
**삽입정렬** : 특정한 데이터를 적절한 위치에 삽입하는 정렬
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
```
시간 복잡도 : O(N^2), 거의 정렬된 상태인 경우 매우 빠르게 동작

## 퀵정렬
**퀵정렬** : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬

**피벗** : 교환하기 위한 기준
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
시간 복잡도 : O(NlogN), 거의 정렬된 상태인 경우 매우 느리게 동작

## 계수정렬
**계수정렬** : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬

**조건** : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있어야 함
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1)
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```
시간 복잡도 : O(N + K), K(최대값의 크기), 데이터의 크기가 한정되어 있고 많이 중복되어 있을 때 유리

## 파이썬 정렬 라이브러리
- `sort(), sorted()` : 병합 정렬 기반, O(NlogN)

## [문제] 위에서 아래로
> 수가 크기에 상관없이 나열되어 있다.
> 내림차순으로 정렬하는 프로그램을 만드시오.

-> 정렬 라이브러리 이용, reverse 사용하여 내림차순 정렬
```python
# 내 풀이
n = int(input())

array = [0] * n
for i in range(n):
    array[i] = int(input())

array.sort(reverse=True)

for data in array:
    print(data, end=' ')
```
## [문제] 성적이 낮은 순서로 학생 출력하기
> N명의 학생 정보는 이름과 성적으로 구분된다.
> 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

-> 정렬 라이브러리 이용, lambda 사용하여 특정 기준으로 정렬
```python
# 내 풀이
n = int(input())
array = []
for i in range(n):
    name, score = input().split()
    array.append([name, int(score)])

array = sorted(array, key=lambda k:k[1])

for data in array:
    print(data[0], end=' ')
```

## [문제] 두 배열의 원소 교체
> A, B 두 배열은 N개의 원소로 구성되어 있으며 모두 자연수이다.
> 최대 K번의 바궈치기 연산을 수행할 수 있다.
> A의 모든 원소 합이 최대가 되도록하는 프로그램을 작성하시오.

-> 정렬 라이브러리 이용, swap 사용
```python
# 내 풀이
n, k = map(int, input().split())
arrayA = sorted(list(map(int, input().split())))
arrayB = sorted(list(map(int, input().split())), reverse=True)

12345
54432
for i in range(k):
    if arrayA[i] >= arrayB[i]: break
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]

print(sum(arrayA))
```