def searchRange(nums: List[int], target: int) -> List[int]:
    res = [-1, -1]
    res[0] = searchFirstIndex(nums, target)
    res[1] = searchLastIndex(nums, target)
    return res

def searchFirstIndex(nums, target):
    index = -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            index = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return index

def searchLastIndex(nums, target):
    index = -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            index = mid
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return index

