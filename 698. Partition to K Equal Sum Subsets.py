# backtrack TLE
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k:
        return False
    
    n = len(nums)
    target = sum(nums) // k
    used = [False] * n

    def dfs(i, k, subsetSum):
        if k == 0:
            return True
        if subsetSum == target:
            return dfs(0, k-1, 0)

        for j in range(i, n):
            if used[j] or subsetSum+nums[j] > target:
                continue
            
            used[j] = True
            if dfs(j+1, k, subsetSum+nums[j]):
                return True
            used[j] = False
        
        return False

    return dfs(0, k, 0)

# bit mask, dp
def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    if sum(nums) % k:
        return False
    
    n = len(nums)
    target = sum(nums) // k
    mask = 0

    @cache
    def dfs(i, k, subsetSum, mask):
        if k == 0:
            return True
        if subsetSum == target:
            return dfs(0, k-1, 0, mask)

        for j in range(i, n):
            if mask & 1<<j or subsetSum+nums[j] > target:
                continue
            
            if dfs(j+1, k, subsetSum+nums[j], mask | 1<<j):
                return True
        
        return False

    return dfs(0, k, 0, mask)
