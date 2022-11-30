'''
프로그래머스
2022 KAKAO TECH INTERNSHIP 성격 유형 검사하기

2:50~3:10
점수 같으면 사전순. 
라이언,튜브 / 콘,프로도 / 제이지,무지 / 어피치,네오
"RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"

dict으로 8개 만들고. 
점수 다 더하고.
점수 큰거 순서대로 출력
'''
def solution(survey, choices):
    answer = ''
    dict = {"R":0,"T":0,"F":0,"C":0,"M":0,"J":0,"A":0,"N":0}
    
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        if choices[i] == 1 or choices[i] == 2 or choices[i] == 3:
            dict[survey[i][0]] += (4 - choices[i])
        else:
            dict[survey[i][1]] += (choices[i] - 4)
    
    dx = ["RT", "FC", "MJ", "AN"]
    for j in range(4):
        if dict[dx[j][0]] > dict[dx[j][1]]:
            answer += dx[j][0]
        elif dict[dx[j][0]] < dict[dx[j][1]]:
            answer += dx[j][1]
        else:
            # 사전순
            answer += min(dx[j][0], dx[j][1])
    
    return answer