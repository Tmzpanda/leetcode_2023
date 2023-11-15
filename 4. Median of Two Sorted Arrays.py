def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(A), len(B)
    p1, p2 = 0, 0
    left, right = -1, -1
    for i in range((m + n) // 2 + 1):    # binary search: mid = (start + end) // 2
        left = right
        if isFirstSmaller(A, p1, B, p2):
            right = A[p1]
            p1 += 1
        else:
            right = B[p2]
            p2 += 1

    if (m + n) % 2 == 1:
        return right
    return (left + right) / 2

def isFirstSmaller(A, p1, B, p2):
    if p1 > len(A) - 1:
        return False
    if p2 > len(B) - 1:
        return False
    return A[p1] <= B[p2]
        
