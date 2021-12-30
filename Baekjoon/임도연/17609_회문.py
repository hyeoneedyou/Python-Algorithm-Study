n = int(input())
words = [input() for _ in range(n)]


def check_palindrome(word):
    mismatch = 0  # 삭제한 문자 개수
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] == word[right]:  # 맨 앞과 맨 뒤가 같은 경우 -> 보장된 부분은 슬라이싱
            left += 1
            right -= 1
        else:  # 맨 앞과 맨 뒤가 다른 경우
            mismatch = 1
            if word[left + 1] == word[right]:  # 맨 뒤가 보장되는 경우
                left += 2
                right -= 1
            elif word[left] == word[right - 1]:  # 맨 앞이 보장되는 경우
                left += 1
                right -= 2
            else:
                mismatch = 2
                break

    return mismatch


for i in range(n):
    print(check_palindrome(words[i]))
