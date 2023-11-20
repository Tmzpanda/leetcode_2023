from collections import deque
class Firstunique_dict:
    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.unique_dict = {}
        for num in nums:
            self.add(num)

    def showFirstunique_dict(self) -> int:
        while self.queue:
            head = self.queue[0]
            if self.unique_dict[head]:
                return head
            else:
                self.queue.popleft()
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)

        if value not in self.unique_dict:
            self.unique_dict[value] = True
        else:
            self.unique_dict[value] = False


