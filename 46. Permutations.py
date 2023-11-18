def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    def dfs(index):
        if index == n:
            res.append(list(nums))

        for i in range(index, n):
            nums[index], nums[i] = nums[i], nums[index] # backtrack
            dfs(index+1)
            nums[index], nums[i] = nums[i], nums[index]

    dfs(0)
    return res
