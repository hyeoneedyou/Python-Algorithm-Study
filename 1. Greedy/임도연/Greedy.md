# 그리디
> 현재 상황에서 지금 당장 좋은 것만 고르는 방법

## [문제] 거스름돈
> 거스름돈으로 500, 100, 50, 10원짜리 동전이 무한히 존재한다고 한다.
> 거슬러 줘야 할 돈이 N원일 때, 거슬러 줘야 할 동전의 최소 개수를 구하라.
> 단, N은 항상 10의 배수이다.

-> 가장 큰 화폐 단위부터 돈을 거슬러 주는 방식으로 해결
```py
# 교재 풀이
n = 1260
count = 0

coins_types = [500, 100, 50, 10]

for coin in coins_types:
    count += n // coin
    n %= coin

print(count)
```
```python
# 내 풀이
n = int(input())

m = [500, 100, 50, 10]
cnt = 0

for i in m:
    if n == 0:
        break
    cnt += n // i
    n %= i

print(cnt)
```
화폐의 종류만큼 반복을 수행 => 시간 복잡도 O(N)

## 그리디 알고리즘의 정당성
> 대부분의 문제는 그리디 알고리즘을 이용했을 대 최적의 해를 찾을 수 없을 가능성이 높다.
> 따라서 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다.

_실제로 거스름돈 문제에서 동전의 단위가 서로 배수 형태가 아니라, 무작위로 주어진 경우에는 그리디 알고리즘으로 해결할 수 없다._

## [문제] 큰 수의 법칙
> 이 문제의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
> 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
> 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
> 이벽값으로 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

-> 반복되는 수열에 대해서 파악해야한다.
```python
# 교재 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

count = int(m / (k + 1)) * k
count += m & (k + 1)

result = 0
result = count * first
result += (m - count) * second

print(result)
```
```python
# 내 풀이
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
f = array[-1]  # 가장 큰 수
s = array[-2]  # 두번째로 큰 수

result = f * (m // k) * k + s * (m % k)

print(result)
```

## [문제] 숫자 카드 게임
> 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수를 의미한다.
> 뽑을 카드의 행을 선택하고 그중 가장 숫자가 낮은 카드를 선택한다.
> 여러 경우의 수 중에서 가장 높은 숫자의 카드를 구하라.

-> 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다.
```python
# 교재 풀이 => 공간효율적
n, m = map(int, input().split())

result = 0
for i in range(n):
        data = list(map(int, input().split()))
        min_value = min(data)
        result = max(result, min_value)

print(result)
```
```python
n, m = map(int, input().split())

array = []
min_array = []
for i in range(n):
        array.append(list(map(int, input().split())))
        min_array.append(min(array[-1]))

print(max(min_array))
```

## [문제] 1이 될 때까지
> 어떠한 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행하려한다.
> 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
> 1. N에서 1을 뺀다.
> 2. N을 K로 나눈다.
> 
> N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하여라.

-> 최대한 많이 나누기를 수행한다.
```python
# 교재 풀이 => 효율적
n, k = map(int, input().split())

result = 0
while True:
    target = (n // k) * k
    result += n - target  # 1번
    n = target

    if n < k:
        break
    result += 1
    n //= k  # 2번

result += (n - 1)

print(result)
```
```python
# 내 풀이
n, k = map(int, input().split())

cnt = 0
while n != 1:
    if n % k != 0:
        n -= 1
    else:
        n //= k
    cnt += 1

print(cnt)
```