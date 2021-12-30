n = int(input())
words = [input() for _ in range(n)]


def is_pseudo(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            is_left_pseudo = is_pseudo(word, left + 1, right)
            is_right_pseudo = is_pseudo(word, left, right - 1)
            if is_left_pseudo or is_right_pseudo:
                return 1
            else:
                return 2
    return 0


for i in range(n):
    print(check_palindrome(words[i]))
