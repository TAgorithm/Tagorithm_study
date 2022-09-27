t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split()) # 4, 2 
    priority = list(map(int, input().split())) # [1 2 3 4] 2341 3412 4123 123 231 312 
    idx = [i for i in range(n)] # [0, 1, 2, 3] [0 1 target 3] 1t30 t301 301t 01t 1t0 t01 
    idx[m] = 'target' # idx[2] = 'target'
    cnt = 0 # 1 2
 
    while priority:
        if priority[0] == max(priority):    
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            priority.pop(0)
            idx.pop(0)
        else:
            priority.append(priority.pop(0))
            idx.append(idx.pop(0))