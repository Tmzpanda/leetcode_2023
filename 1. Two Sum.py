# O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for i, num in enumerate(nums):
        if target - num in num_dict:
            return [num_dict[target - num], i]
        num_dict[num] = i

    return []
