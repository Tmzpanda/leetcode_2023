# dfs TLE
def canJump(nums: List[int]) -> bool:
    n = len(nums)

    memo = {}
    def dfs(i):
        if i == n-1: return True
        if nums[i] == 0: return False
        if i in memo:
            return memo[i]

        for j in range(i+1, min(i+nums[i], n-1)+1):
            if dfs(j):
                memo[i] = True
                return True

        memo[i] = False
        return False

    return dfs(0)

# greedy
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    valid_index = n - 1

    for i in range(n-2, -1, -1):
        if i + nums[i] >= valid_index:
            valid_index = i

    return valid_index == 0
  
