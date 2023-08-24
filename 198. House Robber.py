# dfs
def rob(nums: List[int]) -> int:
    n = len(nums)
    memo = {}
    def dfs(i):
        # memo
        if i in memo: 
            return memo[i]
        # base
        if i >= n:
            return 0

        memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        return memo[i]

    return dfs(0)

# dp
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    
    return dp[n-1]

# space optimization
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]

    prev_prev = nums[0]
    prev = max(nums[0], nums[1])
    
    for i in range(2, n):
        curr = max(nums[i] + prev_prev, prev)
        prev_prev, prev = prev, curr
         
    return prev

