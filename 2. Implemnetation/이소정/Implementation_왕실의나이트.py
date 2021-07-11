place = input()
now = [ord(place[0])-96, int(place[1])] # row, col
count = 0

dirs = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for dir in dirs:
  future = [now[0] + dir[0], now[1] + dir[1]]
  if ((future[0] >= 1 and future[0] <=8) and (future[1] >= 1 and future[1] <= 8)):
    count += 1

print(count)

