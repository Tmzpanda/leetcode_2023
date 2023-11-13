class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.total = 0
        self.length = 0
        self.window = deque()
      
    def next(self, val: int) -> float:
        if self.length < self.size:
            self.window.append(val)
            self.length += 1
            self.total += val      
        else:
            self.window.append(val)
            self.total -= self.window.popleft()
            self.total += val
            
        return self.total/self.length
