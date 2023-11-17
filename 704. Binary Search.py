# O(logn)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1

def search(nums: List[int], target: int) -> int:
    def binarySearch(l, r):
        if l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binarySearch(mid + 1, r)
            else:
                return binarySearch(l, mid - 1)
        else:
            return -1
            
    return binarySearch(0, len(nums) - 1)
    

