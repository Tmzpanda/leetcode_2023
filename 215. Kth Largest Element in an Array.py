# quick select
def findKthLargest(self, nums: List[int], k: int):      
    k = len(nums) - k  # convert kth largest to kth smallest

    def quickSelect(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]

    return quickSelect(0, len(nums) - 1)

# heap
def findKthLargest(nums: List[int], k: int):      
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
          
    return heappop(heap)



