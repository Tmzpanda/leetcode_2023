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
    l, r = 0, m
    while l <= r:
        i = (l + r) // 2  # nums1
        j = (m + n + 1) // 2 - i  # nums2

        nums1L = nums1[i - 1] if i > 0 else float('-inf')
        nums1R = nums1[i] if i < m else float('inf')
        nums2L = nums2[j - 1] if j > 0 else float('-inf')
        nums2R = nums2[j] if j < n else float('inf')

        if nums1L <= nums2R and nums2L <= nums1R:
            if (m + n) % 2 == 0:
                return (max(nums1L, nums2L) + min(nums1R, nums2R)) / 2
            else:
                return max(nums1L, nums2L)
        elif nums1L > nums2R:
            r = i - 1
        else:
            l = i + 1

