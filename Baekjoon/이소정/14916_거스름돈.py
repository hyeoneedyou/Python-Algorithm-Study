n = int(input())

if (n == 1 or n == 3) :
  result = -1
elif (n % 5 == 0) : # 5의 배수이면
  five = n // 5 
  result = five
elif (n % 2 == 0) : # 2의 배수이면
  two = n // 2
  result = two
else :
  five = n // 5
  two = (n % 5) // 2
  result = five + two
print(result)


# n = int(input())

# if (n == 1 or n == 3) :
#   result = -1
# elif (n % 5) % 2 == 0 : 
#   result = n // 5 + (n % 5) // 2
# else :
#   result = ((n // 5) - 1) + ((n % 5 + 5) // 2)

# print(result)