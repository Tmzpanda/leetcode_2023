# O(n) space
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    nums_set = set(nums)
        
    return [target for target in range(1, n + 1) if target not in nums_set]
    
    
# O(1) space
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    n = len(nums)
    for num in nums:
        i = abs(num) - 1
        nums[i] = -abs(nums[i])   # mark the corresponding entries as negative
      
    return [i + 1 for i in range(n) if nums[i] > 0]
  
