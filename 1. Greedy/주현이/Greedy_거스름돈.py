n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 가지고 있는 동전 중에서 큰 단위가 하상 작은 단위의 배수이므로 작은 다위의 동전들을 종합해 다른 해가 나올 수 없기 때문에 가능한 풀이