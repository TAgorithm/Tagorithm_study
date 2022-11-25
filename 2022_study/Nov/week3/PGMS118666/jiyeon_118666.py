def ctype(string):
    if string == 'RT':
        return (0, 0)
    elif string == 'TR':
        return (0, 1)
    elif string == 'CF':
        return (1, 0)
    elif string == 'FC':
        return (1, 1)
    elif string == 'JM':
        return (2, 0)
    elif string == 'MJ':
        return (2, 1)
    elif string == 'AN':
        return (3, 0)
    elif string == 'NA':
        return (3, 1)

def solution(survey, choices):
    answer = ''
    count = [[0,0] for i in range(4)]
    character = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    for i in range(len(choices)):
        idx1, idx2 = ctype(survey[i])
        if choices[i] > 4:
            count[idx1][1-idx2] += choices[i]-4
        else:
            count[idx1][idx2] += 4-choices[i]
    for i in range(4):
        if count[i][0] >= count[i][1]:
            answer += character[i][0]
        else:
            answer += character[i][1]

    return answer