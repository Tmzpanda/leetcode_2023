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

# quick sort
# TLE
def sortArray(nums: List[int]) -> List[int]:
    def quickSort(arr, l, r):
        if l < r:
            p = partition(arr, l, r)
            quickSort(arr, l, p - 1)
            quickSort(arr, p + 1, r)

        return arr

    def partition(arr, l, r):
        pivot = arr[r]
        p = l
        for i in range(l, r):
            if arr[i] <= pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[p], arr[r] = arr[r], arr[p]
        return p

    return quickSort(nums, 0, len(nums) - 1)
        
# quick sort
def sortArray(nums: List[int]) -> List[int]:
    def quickSort(arr, start, end):
        if start < end:      
            # partition
            pivot = arr[random.randint(start, end)]
            l, r = start, end
            while l <= r:
                if arr[l] >= pivot and arr[r] <= pivot:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r -= 1
                elif arr[l] < pivot:
                    l += 1
                else:
                    r -= 1
            quickSort(arr, start, r)
            quickSort(arr, l, end)

        return arr

    return quickSort(nums, 0, len(nums) - 1)
