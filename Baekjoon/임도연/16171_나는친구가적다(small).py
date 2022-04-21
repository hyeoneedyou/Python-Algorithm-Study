sentence = input()
keyword = input()

result = ""
for char in sentence:
    if not char.isdigit():
        result += char

if keyword in result:
    print(1)
else:
    print(0)