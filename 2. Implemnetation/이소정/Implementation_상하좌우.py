board = int(input())
place_x = 1
place_y = 1
gogo = input().split()

for go in gogo :
  if (go == "R") :
    if (place_y >= board) :
      continue
    place_y += 1
  elif (go == "L") :
    if (place_y <= 1) :
      continue
    place_y -= 1
  elif (go == "U") :
    if (place_x <= 1) :
      continue
    place_x -= 1
  else :
    if (place_x >= board) :
      continue
    place_x += 1

print(place_x, place_y)
