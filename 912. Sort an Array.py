# O(nlogn) O(n)
def mergeSort(nums: List[int]) -> List[int]:
    # base
    if len(nums) == 1:
        return nums
    
    # d&q
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    # merge
    merged = [] 
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
          
    merged.extend(left[i:])
    merged.extend(right[j:])
  
    return merged 


# O(nlogn) O(1)
def quickSort(nums, start, end):
    # base
    if start >= end:      
        return

    # partition
    l, r = start, end
    pivot = random.randint(l, r)
    while l <= r:
        while l <= r and nums[l] < nums[pivot]:
            l += 1
        while l <= r and nums[r] > nums[pivot]:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
    # d&q
    quickSort(nums, start, r)
    quickSort(nums, l, end)
    
    
    
    
    
