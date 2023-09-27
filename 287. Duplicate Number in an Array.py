def findDuplicate(nums: List[int]) -> List[int]:
    for num in nums:
        i = abs(num) - 1
      
        if nums[i] < 0:
            return abs(num)
        nums[i] = -nums[i]
