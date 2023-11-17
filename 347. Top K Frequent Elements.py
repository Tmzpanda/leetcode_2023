# sort O(nlogn)
def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_dict = defaultdict(int)
    res = []

    for num in nums:
        freq_dict[num] += 1
      
    items = sorted(freq_dict.items(), key=lambda x: -x[1])
    for i in range(k):
        res.append(items[i][0])

    return res


# heap O(nlogk)
from heapq import heappush, heappop
def topKFrequent(nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        res = []

        for num in nums:
            freq_dict[num] += 1

        heap = []
        for num, freq in freq_dict.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        
        res = []
        while heap:
            _, num = heappop(heap)
            res.append(num)
        res.reverse()

        return res
