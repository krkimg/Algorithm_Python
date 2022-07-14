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

    answer.append(6-count-count2,6-count)
              
    return answer