n = int(input())
boxes = list(map(int, input().split()))

result = [boxes[0]]


def replaceBox(list, box):
    for i in range(len(list)):
        idx = i
        if list[i] > box:
            break
        array = list[:idx + 1]
    array.append(box)

    return array


for box in boxes[1:]:
    result = replaceBox(result, box)

print(len(result))