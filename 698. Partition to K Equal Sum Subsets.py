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

# 
