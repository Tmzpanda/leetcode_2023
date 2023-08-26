# heap
def findKthLargest(nums: List[int], k: int):      
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
          
    return heappop(heap)

# quick select

