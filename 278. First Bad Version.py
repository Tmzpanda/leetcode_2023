def firstBadVersion(n: int) -> int:
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if isBadVersion(mid):
            index = mid
            r = mid - 1
        else:
            l = mid + 1
    return index
