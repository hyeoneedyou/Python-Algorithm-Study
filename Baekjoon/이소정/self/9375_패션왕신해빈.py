# headgear -> hat turban
# eyewear -> sunglasses

# hat
# turban
# sunglasses
# hat + sunglasses
# turban + sunglasses

test = int(input())
for _ in range(test):
  n = int(input())
  all = [["", ""]]
  for _ in range(n):
    cloth = list(map(str, input().split()))
    for i in range(len(all)):
      if cloth[1] == all[i][0]:
        all[i].append(cloth[0])
        # print("in")
        break
      else:
        if i == len(all)-1:
          cloth.reverse()
          all.append(cloth)
          # print("not in")
  sum = 0
  multiply = 1
  if len(all) == 2:
    sum += len(all[1])-1
  else :
    for j in range(1, len(all)):
      multiply *= len(all[j])
    sum = multiply -1 # 알몸인 경우 한 가지 제외
  print(sum)
