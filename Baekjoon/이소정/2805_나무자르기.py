n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while(start <= end) :
  height = (start + end) // 2
  count = 0
  # for i in tree :
  #   if ( i-height > 0) :
  #     count += (i-height)
  count = sum([i-height if (i-height) > 0 else 0 for i in tree])
  if count >= m :
    start = height + 1
  else :
    end = height - 1

print(end)
