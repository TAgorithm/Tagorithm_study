import sys
import itertools

n = int(input())

numlist = list(map(int, sys.stdin.readline().split()))

max_diff = 0

permulist = list(itertools.permutations(numlist, n))


def sum_diff(arr, idx1, idx2):
    if idx1 == len(arr) - 1:
        return 0
    diff = abs(arr[idx1] - arr[idx2])
    return diff + sum_diff(arr, idx1+1, idx2+1)


for i in range(len(permulist)):
    max_diff = max(sum_diff(permulist[i], 0, 1), max_diff)

print(max_diff)
