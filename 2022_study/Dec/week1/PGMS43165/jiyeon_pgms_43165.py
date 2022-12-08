from itertools import combinations
def combination_cnt(numbers, target):
    s = sum(numbers)
    cnt = 0
    for i in range(1, len(numbers)+1):
        com = list(combinations(numbers, i))
        for j in range(len(com)):
            ans = s - (sum(com[j]) * 2)
            if ans == target:
                cnt += 1
    return cnt

# numbers = [1,1,1,1,1]
# target = 3

numbers = [4,1,2,1]
target = 4

print(combination_cnt(numbers, target))