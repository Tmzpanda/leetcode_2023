# dfs
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]

    def dfs(nums, i, memo):
        if i in memo:
            return memo[i]
        if i >= n-1:
            return 0

        memo[i] = max(nums[i] + dfs(nums, i+2, memo), dfs(nums, i+1, memo))
        return memo[i]

    return max(
        dfs(nums[1:], 0, {}), 
        dfs(nums[:-1], 0, {})
        ) 

# dp
def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]
    if n == 2: return max(nums[0], nums[1])

    def rob(nums):
        dp = [0]*(n-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[n-2]

    return max(rob(nums[:-1]), rob(nums[1:]))

# space optimization
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]
    if n == 2: return max(nums[0], nums[1])

    def rob(nums):
        prev_prev = nums[0]
        prev = max(nums[0], nums[1])
        for i in range(2, n-1):
            curr = max(nums[i] + prev_prev, prev)
            prev_prev, prev = prev, curr

        return prev

    return max(rob(nums[:-1]), rob(nums[1:]))
