"""
num    maxheap    minheap
1      1              
0                 0
       0          1
2      2, 0       1
       1, 0       2

maxheap keeps track of LOWER bound of median
minheap                HIGHER bound

"""
class MedianFinder:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        m, n = len(self.maxheap), len(self.minheap)
        if m == n:
            heappush(self.maxheap, -num)
        if m > n:
            heappush(self.minheap, num)
        
        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))
    
    def findMedian(self) -> float:
        m, n = len(self.maxheap), len(self.minheap)
        if m == n:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0]
