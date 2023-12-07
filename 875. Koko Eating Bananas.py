def minEatingSpeed(piles: List[int], h: int) -> int:
    def timeToFinish(piles, speed):
        time = 0
        for p in piles:
            time += math.ceil(p/speed)
        return time

    l, r = 1, max(piles)
    while l <= r:
        mid = (l+r) // 2
        if timeToFinish(piles, mid) > h:
            l = mid + 1
        else:
            index = mid
            r = mid - 1

    return index
