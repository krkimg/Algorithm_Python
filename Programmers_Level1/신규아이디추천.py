def solution(numbers):
    answer = 0
    numbers.sort()
    num=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        if numbers[i] in num:
            num.remove(numbers[i])
            
    for i in range(len(num)):
        answer+=num[i]        
    
    return answer