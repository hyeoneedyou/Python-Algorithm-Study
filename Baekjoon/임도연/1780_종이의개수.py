n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

fill_with_minus = 0
fill_with_zero = 0
fill_with_plus = 0


def is_all_same_num(target):  # 매개변수로 들어온 종이가 모두 같은 수로 되어있는지 확인
    if type(target) == int:  # 숫자 하나
        return target
    else:  # 2차원 배열
        target_size = len(target)
        base_num = target[0][0]

        for i in range(target_size):
            for j in range(target_size):
                if target[i][j] != base_num:
                    return 2
        return base_num


def cut_with_nine(target):
    target_size = len(target)
    cut_size = target_size // 3
    new_cut_list = []

    if cut_size == 1:  # 3x3인 경우 => 한 개씩 쪼개면 된다
        for i in range(target_size):
            for j in range(target_size):
                new_cut_list.append(target[i][j])
    else:  # 자르는 크기대로 나눠서 넣어야 한다
        for x in range(3):
            for y in range(3):
                current_paper = []
                # 9 -> 3 / 27 -> 9
                for i in range(x * cut_size, (x + 1) * cut_size):
                    current_row = []
                    for j in range(y * cut_size, (y + 1) * cut_size):
                        current_row.append(target[i][j])
                    current_paper.append(current_row)
                new_cut_list.append(current_paper)
    return new_cut_list


def cut_paper(target):
    num = is_all_same_num(target)

    # 모두 같은 수인 경우
    if num == -1:
        global fill_with_minus
        fill_with_minus += 1
        return
    elif num == 0:
        global fill_with_zero
        fill_with_zero += 1
        return
    elif num == 1:
        global fill_with_plus
        fill_with_plus += 1
        return

    new_paper_list = cut_with_nine(target)
    for new_paper in new_paper_list:
        cut_paper(new_paper)


cut_paper(paper)

print(fill_with_minus)
print(fill_with_zero)
print(fill_with_plus)
