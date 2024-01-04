def solution(storey):
    answer = 0

    nums = [int(i) for i in str(storey)]
    length = len(nums)
    
    for idx in range(length-1, -1, -1):
        if idx == 0:
            if nums[idx] == 0:  # 가장 앞 층이 0이라면 자릿수가 올려진 것이므로 10^n 층이 된 것
                answer += 1  # 마법의 돌 하나로 내려갈 수 있음
            else:
                # 아니라면 n개의 층을 내려가거나, (10-n)개의 층을 올라간 후 10개의 층을 내려가는 형태가 되므로 11-n
                answer += min(nums[idx], 11 - nums[idx])  
        
        # 이외의 경우 4층 이하라면, 내려가는 것이 이득임
        elif nums[idx] <= 4:
            answer += nums[idx]
        
        # 6층 이상이라면 (10 - 현재 층)만큼 마법의 돌을 사용하고, 내려가기 위해 마법의 돌 하나를 쓰는 것이 이득
        elif nums[idx] >= 6:  
            answer += 10 - nums[idx]  # 현재 층에서 사용할 마법의 돌 개수를 더하고
            if idx >= 1:
                nums[idx-1] += 1  # 자리수를 올려두어 나중에 처리함
        
        else:  # 5층이라면 앞 층을 살펴보고 비교해야 함
            
            # 만약 앞 층이 4층 이하라면 올라갔을 때 5층 이하가 되므로 내려가는 것이 낫다. (5층은 앞 층에서 판별한다.)
            # 앞 층이 5층 이상이라면 올라갔을 때 6층 이상이 되므로, 올라가는 것이 이득이 된다.
            if idx >= 1 and nums[idx-1] >= 5:
                nums[idx-1] += 1
            
            answer += 5
    
    return answer