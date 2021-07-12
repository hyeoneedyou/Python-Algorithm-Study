n = int(input())

if (n == 1 or n == 3) :
  result = -1
elif (n % 5) % 2 == 0 : # 7 -> 5 * 1 + 2 * 1
  result = n // 5 + (n % 5) // 2
else : # 8 -> 5 * 0 + 2 * 4 
  result = ((n // 5) - 1) + ((n % 5 + 5) // 2)

print(result)