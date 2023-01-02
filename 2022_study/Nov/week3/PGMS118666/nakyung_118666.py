def solution(survey, choices):
    answer = ''
    
    # 유형 딕셔너리 생성
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 유형 점수 추가
    for i in range(len(survey)):
        disagree = survey[i][0]
        agree = survey[i][1]
        choice = choices[i]
    
        if (choice == 1):
            score[disagree] += 3
        elif (choice == 2):
            score[disagree] += 2
        elif (choice == 3):
            score[disagree] += 1
        elif (choice == 4):
            continue
        elif (choice == 5):
            score[agree] += 1
        elif (choice == 6):
            score[agree] += 2
        else:
            score[agree] += 3
                
    # 지표끼리 비교해서 큰 숫자
    if (score['R'] >= score['T']):
        answer += 'R'
    else: answer += 'T'
    
    if (score['C'] >= score['F']):
        answer += 'C'
    else: answer += 'F'
    
    if (score['J'] >= score['M']):
        answer += 'J'
    else: answer += 'M'
    
    if (score['A'] >= score['N']):
        answer += 'A'
    else: answer += 'N'
    
    return answer