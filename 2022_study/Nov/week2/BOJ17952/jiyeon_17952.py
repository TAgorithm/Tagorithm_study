import sys

N = int(sys.stdin.readline())
assignlist = []
sum = 0
for _ in range(N):
    assignment = list(map(int, sys.stdin.readline().split()))
    if assignment[0] == 1:
        assignment[2] -= 1
        if assignment[2] == 0:
            sum += assignment[1]
            continue
        assignlist.append(assignment)
    else:
        if len(assignlist) > 0:
            assign = assignlist.pop()
            if assign[0] == 1:
                assign[2] -= 1
            if assign[2] == 0:
                sum += assign[1]
                continue
            assignlist.append(assign)

print(sum)
