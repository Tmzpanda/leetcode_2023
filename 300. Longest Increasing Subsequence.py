# dfs
def lengthOfLIS(nums: List[int]) -> int:
     n = len(nums)
     memo = {}
     def dfs(i):
         if i in memo:
             return memo[i]

         memo[i] = 1
         for j in range(0, i):
             if nums[j] < nums[i]:
                 memo[i] = max(memo[i], dfs(j)+1)
         return memo[i]

     s = 1
     for i in range(n):
         s = max(s, dfs(i))
         
     return s

# dp O(n^2)
"""
 0  1  2  3
[1, 2, 4, 3]

LIS[0] = 1
LIS[1] = max(1, 1+LIS[0]) = 2
LIS[2] = max(1, 1+LIS[0], 1+LIS[1]) = 3
LIS[3] = max(1, 1+LIS[0], 1+LIS[1]) = 3

"""
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)        
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) 
