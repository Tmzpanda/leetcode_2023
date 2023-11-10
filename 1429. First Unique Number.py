from collections import deque
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.unique = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue:
            head = self.queue[0]
            if self.unique[head]:
                return head
            else:
                self.queue.popleft()
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)

        if value not in self.unique:
            self.unique[value] = True
        else:
            self.unique[value] = False


