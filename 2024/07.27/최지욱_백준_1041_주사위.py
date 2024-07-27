'''
메모리 : 31120KB
시간 : 44ms
'''
def main():
    
    N = int(input())
    nums = list(map(int, input().split()))
    
    ## 1 -> (N-1) * (N-1) * 5
    
    ## 2 -> (N-1) * 4 + (N-2) * 4
    
    ## 3 -> 4
    
    min1 = min(nums)
    min2 = min(nums[0]+nums[1], nums[0]+nums[2], nums[0]+nums[3], nums[0]+nums[4], 
               nums[1]+nums[2],nums[1]+nums[3], nums[1]+nums[5],
               nums[2]+nums[4],nums[2]+nums[5],
               nums[3]+nums[4],nums[3]+nums[5],
               nums[4]+nums[5])
    min3 = min(nums[0]+nums[1]+nums[2],nums[0]+nums[1]+nums[3],nums[0]+nums[2]+nums[4],nums[0]+nums[3]+nums[4],
               nums[1]+nums[2]+nums[5],nums[1]+nums[3]+nums[5],
               nums[2]+nums[4]+nums[5],nums[3]+nums[4]+nums[5])
    
    print(((N-2)**2+(N-2)*(N-1)*4) * min1 + ((N-1)*4+(N-2)*4) * min2 + 4 * min3)
    
if __name__ =='__main__': 
    main()