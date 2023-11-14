#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# recursion
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.array = []
        self.index = -1
        def flatten(nestedList):
            for item in nestedList:
                if item.isInteger():
                    self.array.append(item.getInteger())
                else:
                    flatten(item.getList())    # recursion
                    
        flatten(nestedList)
    
    def next(self) -> int:
        self.index += 1
        return self.array[self.index]
    
    def hasNext(self) -> bool:
        return self.index + 1 < len(self.array)


# queue
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque(nestedList)
        self.next_int = None
        
    def next(self) -> int:
        return self.next_int
        
    def hasNext(self) -> bool:
        while self.queue:
            next_item = self.queue.popleft()
            if next_item.isInteger():
                self.next_int = next_item.getInteger()
                return True
            else:
                self.queue.extendleft(next_item.getList()[::-1])

        return False
