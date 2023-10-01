# O(n)
def findKthPositive(arr: List[int], k: int) -> int:
    i, target = 0, 1
    while i < len(arr):
        if arr[i] == target:
            i += 1
            target += 1
        elif arr[i] > target:
            k -= 1
            if k == 0:
                return target
            target += 1
        else:
            i += 1  # deduplicate

    return arr[-1] + k


# O(logn)
"""
nums[i]
nums[i] - (i+1) denotes #of missing number at given index i

nums[i] =         [1, 3, 4, 6]
nums[i] - (i+1) = [0, 1, 1, 2]

binary search last index so that `nums[i] - (i+1) <= k`

#of missing number between nums[i-1] and nums[i] is k - (nums[i-1] - i),
the kth missing number is nums[i-1] + k - (nums[i-1] - i) = i + k

"""
def findKthPositive(arr: List[int], k: int) -> int:
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        missing = arr[mid] - (mid+1)

        if missing < k:
            l = mid + 1
        else:
            r = mid - 1

    return l + k
    
