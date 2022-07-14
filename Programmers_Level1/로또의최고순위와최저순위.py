def solution(lottos, win_nums):
    answer = []
    count =0
    count2 =0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count+=1


    for i in range(len(lottos)):
        if lottos[i]==0:
            count2+=1
    if count+count2 ==0:
        answer.append(6-count-count2)
    else:
        answer.append(6-count-count2+1)
    if count==0:
        answer.append(6-count)
    else:
        answer.append(6-count+1)

    return answer