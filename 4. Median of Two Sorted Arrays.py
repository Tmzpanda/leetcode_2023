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
