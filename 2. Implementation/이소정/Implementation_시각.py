N = int(input())
count = 0

for hour in range(N+1) :
  for min in range(60):
    for sec in range(60):
      full_time = str(hour) + str(min) + str(sec)
      if "3" in full_time :
        count += 1

print(count)