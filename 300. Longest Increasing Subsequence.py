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

dp[0] = 1
dp[1] = max(1, 1+dp[0]) = 2
dp[2] = max(1, 1+dp[0], 1+dp[1]) = 3
dp[3] = max(1, 1+dp[0], 1+dp[1]) = 3

dp[i] denotes length of LIS at index i
"""
def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)        
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) 


# binary search
def lengthOfLIS(nums: List[int]) -> int:
    def searchInsert(nums, target) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

    arr = [nums[0]]
    for num in nums[1:]:
        i = searchInsert(arr, num)
        if i == len(arr):
            arr.append(num)     #
        else:
            arr[i] = num

    return len(arr)
