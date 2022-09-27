word = input()
word_list = []

for _ in word:
    word_list.append(word)
    word = word[1:]

for i in sorted(word_list):
    print(i)      