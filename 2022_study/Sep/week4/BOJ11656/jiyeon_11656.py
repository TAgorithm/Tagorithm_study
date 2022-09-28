str1 = input()

arr = []

for i in range(len(str1)):
    arr.append(str1[i:])

arr.sort()

for str1 in arr:
    print(str1)