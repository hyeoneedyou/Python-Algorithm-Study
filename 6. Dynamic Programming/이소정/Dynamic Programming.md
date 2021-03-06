# 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘

## 중복되는 연산을 줄이자

- 컴퓨터를 활용해도 해결하기 어려운 문제 : 최적의 해를 구하기에 시간이 매우 많이 필요하거나 메모리 공간이 매우 많이 필요한 문제
- 컴퓨터는 연산 속도에 한계가 있고, 메모리 공간을 사용할 수 있는 데이터의 개수도 한정적이라는 점이 많은 제약을 발생시킴
- 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 작성해야 함
- 어떤 문제는 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는 방법이 있음. 대표적인 방법이 다이나믹 프로그래밍(Dynamic Programming) 기법으로 동적 계획법이라고 표현하기도 함

```
<다이나믹 프로그래밍과 동적 할당의 다이나믹은 같은 의미일까?>
프로그래밍에서 다이나믹은 '프로그램이 실행되는 도중에'라는 의미이다. 예를 들어 자료구조에서 동적 할당(Dynamic Allocation)은 프로그램 실행 중에 프로그램 실행에 필요한 메모리를 할당하는 기법이다. 하지만 다이나믹 프로그래밍에서의 '다이나믹'은 이런 의미가 아니라는 것 정도만 기억하자
```

- 피보나치 수열을 재귀 함수로 사용하면 심각한 문제가 생길 수 있음. f(n) 함수에서 n이 커지면 커질수록 수행 시간이 기하급수적으로 늘어나기 때문임. 이 소스코드의 시간 복잡도는 O(2^n)임. f(6)을 호출할 때 동일한 함수가 반복적으로 호출되고 계속 호출할 때마다 계산함
- 이처럼 피보나치 수열의 점화식을 재귀 함수를 사용해 만들 수는 있지만, 단순히 매번 계산하도록 하면 문제를 효율적으로 해결할 수 없음. 이러한 문제는 다이나믹 프로그래밍을 사용하면 효율적으로 해결할 수 있음
- 다만 항상 다이나믹 프로그래밍을 사용할 수 없으며, 다음 조건을 만족해야 함

```
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
```

- 피보나치 수열은 이러한 조건을 만족하는 대표 문제임. 이 문제를 메모이제이션(Memoization) 기법을 사용해서 해결해보자. 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법을 의미함
- 메모이제이션은 값을 저장하는 방법이므로 캐싱(Cashing) 이라고도 함
- 실제로 메모이제이션은 어떻게 구현될 수 있을까 : 한 번 구한 정보를 리스트에 저장하는 것. 다이나믹 프로그래밍을 재귀적으로 수행하다가 같은 정보가 필요할 때는 이미 구한 정답을 그대로 리스트에서 가져오면 됨

```python
# 한 번 계산한 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):

  # 종료 조건(1 혹은 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1

  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]

  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo(x - 1) + fibo(x - 2)
  return d[x]

print(fibo(99))
```

<br>

- 다이나믹 프로그래밍이란 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘 기법
- 퀵 정렬은 정렬을 수행할 때 정렬한 리스트를 분할하며 전체적으로 정렬이 될 수 있도록 하고, 분할 정복(Divide and Conquer) 알고리즘으로 분류함
- 둘의 차이점은 다이나믹 프로그래밍은 문제들이 서로 영향을 미치고 있다는 점
- 퀵 정렬은, 한 번 기준 원소(Pivot)가 자리를 변경해서 자리를 잡게 되면 그 기준 원소의 위치는 더 이상 바뀌지 않고 그 피벗값을 다시 처리하는 부분 문제는 존재하지 않음
- 반면에 다이나믹 프로그래밍은 한 번 해결했던 문제를 다시금 해결한다는 점이 특징. 그렇기 때문에 이미 해결된 부분 문제에 대한 답을 저장해 놓고, 이 문제는 이미 해결이 됐던 것이니까 다시 해결할 필요가 없다고 반환함
- 일반적으로 재귀 함수보다 반복문을 이용한 다이나믹 프로그래밍이 더 성능이 좋음
- 다이나믹 프로그래밍을 적용했을 때의 피보나치 수여 알고리즘의 시간 복잡도는 O(N)
- 재귀 함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법을, 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 `탑다운(Top-Down) 방식`이라고 함
- 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차큰차큰 답을 도출한다고 하여 `보텀업(Bottom-Up) 방식`이라고 함

```python
# 앞서 계산한 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
  d[i] = d[i - 1] + d[i - 2]

print(d[n])
```

<br>

- 탑다운(메모이제이션) 방식은 '하향식'이라고도 하며, 보텀업 방식은 '상향식'이라고 함
- 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식임. 보텀업 방식에서 사용되는 결과 저장용 리스트는 'DP 테이블'이라고 부르며, 메모이제이션은 탑다운 방식에 국한되어 사용되는 표현임.
- 다이나믹 프로그래밍과 메모이제이션의 개념을 혼용해서 사용하는 경우도 있는데, 엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓은 넓은 개념을 의미하므로, 다이나믹 프로그래밍과는 별도의 개념임. 한 번 계산된 결과를 어딘가에 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음
- 수열은 배열이나 리스트로 표현할 수 있다로 했는데, 메모이제이션은 때에 따라서 다른 자료형, 예를 들어 사전(dict) 자료형을 이용할 수도 있음. 사전 자료형은 수열처럼 연속적이지 않은 경우에 융요한데, 예를 들어 a(n)을 계산하고자 할 때 a0~a(n-1) 모두가 아닌 일부의 작은 문제에 대한 해답만 필요한 경우가 존재할 수 있음. 이럴 때에는 사전 자료형을 사용하는게 더 효과적임
  <br>

## 문제

<details>
  <summary>1로 만들기</summary>
  <div markdown="1">

Q. 정수 X가 주어질 때 정수 X가 사용할 수 있는 연산은 다음과 같이 4기자이다.

```
1. X가 5로 나누어떨어지면, 5로 나눈다.
2. X가 3으로 나누어떨어지면, 3으로 나눈다.
3. X가 2로 나누어떨어지면, 2로 나눈다.
4. X에서 1을 뺀다.
```

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
예를 들어 정수가 26이면 다음과 같이 계산해서 3번의 연산이 최솟값이다.

1. 26 - 1 = 25
2. 25 / 5 = 5
3. 5 / 5 = 1

<br>

`입력 조건` :

- 첫째 줄에 정수 X가 주어진다. (1 <= X <= 30,000)

<br>

`출력 조건` :

- 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

<문제해설>

- 가지고 있던 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없음
- 가장 큰 단위의 화폐부터 가장 작은 단위의 화폐까지 차례대로 확인하여 거슬러 주는 작업만을 수행하면 됨 -> 정당함
- 대부분의 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 함

  </div>
</details>

<details>
  <summary>개미 전사</summary>
  <div markdown="1">

Q. 개미 전사는 메뚜기 마을의 식량창고를 몰래 공격하려고 한다. 메뚜기 마을에는 여러 개의 식량창고가 있는데 식량창고는 일직선으로 이어져 있다. 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다. 이때 메뚜리 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다. 따라서 개미 전사는 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다. 예를 들어 식량창고 4개가 다음과 같이 존재한다고 가정하자.

```
{1, 3, 1, 5}
```

이때 개미 전사는 두 번째 식량창고와 네 번째 식량창고를 선택했을 때 최댓값인 총 8개의 식량을 빼앗을 수 있다. 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원한다. 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.<br>

`입력 조건` :

- 첫째 줄에 식량창고의 개수 N이 주어진다. (3 <= N <= 100)
- 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다. (O <= K <= 1,000) <br>

`출력 조건` :

- 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.

<문제해설>

```
1. (i - 1)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 없다.
2. (i - 2)번째 식량창고를 털기로 결정한 경우 현재의 식량창고를 털 수 있다.
```

- 위의 두 경우 중 더 많은 식량을 털 수 있는 경우를 선택하면 된다.
- i번째 식량창고에 대한 최적의 해를 구할 때 왼쪽부터 (i - 3)번째 이하의 식량창고에 대한 최적의 해에 대해서는 고려할 필요가 없다. 예를 들어 d[i - 3]는 d[i - 1]과 d[i - 2]을 구하는 과정에서 이미 계산되었기 때문에, d[i]의 값을 구할 때는 d[i - 1]과 d[i - 2]만 고려하면 된다. 따라서 i번째 식량창고에 있는 식량의 양이 k_i라고 했을 때 점화식은 다음과 같다.
- `a_i = max(a_i-1, a_i-2 + k_i)`

  </div>
</details>

<details>
  <summary>바닥 공사</summary>
  <div markdown="1">

가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 이 얇은 바닥을 1 X 2의 덮개, 2 X 1의 덮개, 2 X 2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 2 X 3 크기의 바닥을 채우는 경우의 수는 5가지이다.

`입력 조건` :

- 첫째 줄에 N이 주어진다. (1 <= N <= 1,000)<br>

`출력 조건` :

- 첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.

<문제해설>

```
1. 왼쪽부터 i - 1까지 길이가 덮개로 이미 채워져 있으면 2 X 1의 덮개를 채우는 하나의 경우 밖에 존재하지 않는다.
2. 왼쪽부터 i - 2까지 길이가 덮개로 이미 채워져 있으면 1 X 2 덮개 2개를 넣는 경우, 혹은 2 X 2의 덮개 하나를 넣는 경우로 2가지 경우가 존재한다. 참고로 2 X 1 덮개 2개를 넣는 경우를 고려하지 않는 이유는 1에서 이미 해당 경우가 고려되었기 때문이다.
```

- i번째 위치에 대한 최적의 해를 구할 때 왼쪽부터 (i - 3)번째 이하의 위치에 대한 최적의 해에 대해서는 고려할 필요가 없다. 왜냐하면 사용할 수 있는 덮개의 형태가 최대 2 X 2 크기의 직사각형 형태이기 때문이다. 다시 말해 바닥을 채울 수 있는 형태는 위에서 언급한 경우밖에 없다. 따라서 다음과 같은 점화식을 세울 수 있다.
- `a_i = a_i-1 + a_i-2 * 2`
- 왼쪽부터 N - 2까지 길이가 덮개로 이미 채워져 있는 경우 덮개를 채우는 방법은 2가지 경우가 있다.

  </div>
</details>

<details>
  <summary>효율적인 화폐 구성</summary>
  <div markdown="1">

N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

`입력 조건` :

- 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
- 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.<br>

`출력 조건` :

- 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
- 불가능할 때는 -1을 출력한다.

<문제해설>

- 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾아야 한다.
- 금액 i를 만들 수 있는 최소한의 화폐 개수를 a_i, 화폐의 단위를 k라고 했을 때 다음과 같이 점화식을 작성할 수 있다.

  ```
  1. a_i-k를 만드는 방법이 존재하는 경우. a_i = min(a_i, a_i-k + 1)
  2. a_i-k를 만드는 방법이 존재하지 않는 경우. a_i = 10,001
  ```

step1. 초기화
step2. 화폐 단위 : 2 -> 3 -> 5

  </div>
</details>

<br>

## 새로 공부한 부분 & 공부해야 할 부분
