# 프린터 큐
# 나의 풀이

# 테스트케이스의 수
num = int(input())

# 그 수만큼 반복하기
for _ in range(num):
    n, m = list(map(int, input().split())) # 문서의 개수, 어디에 위치하는지    
    # 우선순위 저장
    queue = list(map(int, input().split()))
    # 내 위치 리스트
    idx = list(range(len(queue)))
    idx[m] = "me"
    
    # 나의 순서
    count = 0
    
    while True:
        # 첫 번째 요소가 우선순위 가장 높으면 count +1 해 주기
        if (queue[0] == max(queue)):
            count += 1
            if (idx[0] == "me"):
                print(count)
                break
            else:
                queue.pop(0)
                idx.pop(0)
        # 첫 번째 요소가 우선순위 가장 높은 경우 아닐 때 맨 뒤로
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))