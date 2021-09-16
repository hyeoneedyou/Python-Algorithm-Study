# ()  2
# []  3
# (x)  2*x
# [x]  3*x
# xy  x+y
# (()[[]]) (())[][]

# stack...? -> [] or ()

# 옳은 괄호인가
mark = input()
result = 0
isPossible = mark
while True:
  isPossible = isPossible.replace("()","")
  isPossible = isPossible.replace("[]","")
  if "()" not in isPossible and "[]" not in isPossible:
    break;
if isPossible != "":
  print(0)
else:
  # 괄호의 값 작성하기
  mark = mark.replace("()", "2")
  mark = mark.replace("[]","3")
  # ()
  if "(" in mark and mark[mark.index("(") + 2] == ")":
    num = mark[mark.index("(") + 1]
    print(num)
  # []
  print(mark)
  print(1)

# (2 9)6
# (11)6
# 22 6
# 28
