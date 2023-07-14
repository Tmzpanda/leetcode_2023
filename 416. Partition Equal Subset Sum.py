# O(n*S)
# dfs
def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    subset_sum = total_sum // 2

    memo = {}
    def dfs(i, s):
        if s == 0:
            return True
        if i == 0 or s < 0:
            return False
        if (i, s) in memo:
            return memo[(i, s)]
        
        res = dfs(i - 1, s - nums[i]) or dfs(i - 1, s)

        memo[(i, s)] = res
        return res

    return dfs(n - 1, subset_sum)
    
  
# dp
def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    subset_sum = total_sum // 2

    dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for s in range(subset_sum + 1):
            if nums[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - nums[i-1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
            
    return dp[n][subset_sum]


# space optimization
def canPartition(nums: List[int]) -> bool:
    n = len(nums)
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    subset_sum = total_sum // 2

    dp = [False] * (subset_sum + 1)
    dp[0] = True

    for num in nums:
        for s in range(subset_sum, num - 1, -1):  # iterate backwards
            dp[s] = dp[s] or dp[s - num]

    return dp[subset_sum]
    
