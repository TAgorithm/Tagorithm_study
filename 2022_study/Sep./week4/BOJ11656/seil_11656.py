# 접미사 배열(11656)
# 9:45~9:49

n = input()
words = []
for i in range(len(n)):
    words.append(n[i:])

for v in sorted(words):
    print(v)

