# merge
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    p1, p2 = 0, 0
    l, r = -1, -1 
    # merge
    for i in range((m+n)//2 + 1):
        l = r
        if p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                r = nums1[p1]
                p1 += 1
            else:
                r = nums2[p2]
                p2 += 1
        elif p1 == m:
            r = nums2[p2]
            p2 += 1
        else:
            r = nums1[p1]
            p1 += 1

    if (m+n) % 2 == 1:
        return r
    else:
        return (l+r)/2


# binary search
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)

    l, r = 0, m-1
    while True:
        mid = (l + r) // 2  # nums1
        j = (m + n) // 2 - mid - 2  # nums2

        nums1L = nums1[mid] if mid >= 0 else float('-inf')
        nums1R = nums1[mid+1] if mid+1 < m else float('inf')
        nums2L = nums2[j] if j >= 0 else float('-inf')
        nums2R = nums2[j+1] if j+1 < n else float('inf')

        if nums1L <= nums2R and nums2L <= nums1R:
            # even
            if (m + n) % 2 == 0:
                return (max(nums1L, nums2L) + min(nums1R, nums2R)) / 2
            # odd
            else:
                return min(nums1R, nums2R)
        elif nums1L > nums2R:
            r = mid - 1
        else:
            l = mid + 1
