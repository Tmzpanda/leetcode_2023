# set
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# two pointers
def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    res = []

    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return list(set(res))

# binary search
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    res = []

    for num in nums1:
        if binarySearchFound(nums2, num):
            res.append(num)

    return list(set(res))

def binarySearchFound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return False
