class RandomizedSet:
    def __init__(self):
        self.array = []
        self.lookup = {}
        
    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        self.array.append(val)
        self.lookup[val] = len(self.array)-1
        
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.lookup:
            index = self.lookup[val]
            self.array[index], self.lookup[self.array[-1]] = self.array[-1], index  # O(1) remove in an array

            self.array.pop()
            del self.lookup[val]
            return True

        return False

    def getRandom(self) -> int:
        return self.array[random.randint(0, len(self.array)-1)]
