s = input()
t = input()

result = 0


def game(str):
    global result

    if len(str) == 0:
        return

    if str[-1] == "A":
        ver1 = str[:-1]
        if ver1 == s:
            result = 1
            return
        game(ver1)

    if str[0] == "B":
        ver2 = "".join(reversed(str))[:-1]
        if ver2 == s:
            result = 1
            return
        game(ver2)


game(t)
print(result)

# def game(str):
#     global result
#     ver1 = str + "A"
#     ver2 = "".join(reversed(str + "B"))
#
#     if ver1 == t or ver2 == t:
#         result = 1
#         return
#
#     if len(str) == len(t):
#         return
#
#     game(ver1)
#     game(ver2)
#
#
# if s[0] != t[0] and s[0] != t[-1]:
#     print(result)
#     exit()
#
# game(s)
# print(result)
