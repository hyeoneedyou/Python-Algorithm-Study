balance = int(input("거슬러 줘야 할 돈을 얼마? : ")) # 1260원

five_hundred = balance // 500 # 500원 2개
one_hundred =  (balance % 500) // 100 # 260원 -> 100원 2개 
five_ten = (balance % 100 ) // 50 # 60원 -> 50원 1개
one_ten = (balance % 50 ) // 10 # 10원 -> 10원 1개

sum = five_hundred + one_hundred + five_ten + one_ten

print(sum)

# Solution

# balance = 1260
# count = 0
# list = [500, 100, 50, 10]

# for coin in list:
#   count += balance // coin
#   balance %= coin

# print(count)