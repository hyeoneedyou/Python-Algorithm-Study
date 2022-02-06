n = int(input())
size = [list(map(int, input().split())) for _ in range(n)]
size.sort()
height_array = [size[i][1] for i in range(n)]

# 2 4
# 4 6
# 5 3
# 8 10
# 11 4
# 13 6
# 15 8

save_x_pos = size[0][0]
save_height = size[0][1]
area = 0

i = 1
while i < n:
    x_pos = size[i][0]
    height = size[i][1]
    # 다음 창고 높이가 높은 경우
    # 5 [7] => 7
    if save_height <= height:
        area += save_height * (x_pos - save_x_pos)
        save_height = height
        save_x_pos = x_pos
    else:
        # 다음 창고 높이가 낮은데 이후에 더 높은 창고가 있는 경우
        # [3] 1 2 4 1 => 4
        max_store_height = max(height_array[i:])
        if height < max_store_height:
            max_store_index = i + height_array[i:].index(max_store_height)
            max_store_x_pos = size[max_store_index][0]
            if save_height < max_store_height:
                area += save_height * (max_store_x_pos - save_x_pos)
            else:
                area += max_store_height * (max_store_x_pos - (save_x_pos + 1)) + save_height
            save_height = max_store_height
            save_x_pos = max_store_x_pos
            i = max_store_index + 1
            continue
        # 다음 창고 높이가 낮은데 이후에 더 높은 창고가 없는 경우
        # [3] 2 1
        else:
            area += height * (x_pos - (save_x_pos + 1)) + save_height
            save_x_pos = x_pos
    i += 1
area += height_array[-1]
print(area)
