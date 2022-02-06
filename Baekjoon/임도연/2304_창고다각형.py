n = int(input())
input_size = []

max_height = 1
max_height_index = 0
max_x_pos = 0

for _ in range(n):
    x, h = map(int, input().split())
    input_size.append([x, h])
    if max_x_pos < x:
        max_x_pos = x
    if max_height < h:
        max_height = h
        max_height_index = x

height_array = [0] * (max_x_pos + 1)
for x, h in input_size:
    height_array[x] = h


area = 0
temp_height = 0
for i in range(max_height_index + 1):
    if height_array[i] > temp_height:
        temp_height = height_array[i]
    area += temp_height

temp_height = 0
for i in range(max_x_pos, max_height_index, -1):
    if height_array[i] > temp_height:
        temp_height = height_array[i]
    area += temp_height
print(area)