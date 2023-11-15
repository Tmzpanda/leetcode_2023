class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)] # each bucket is a [] for handling collisions
        
    def put(self, key: int, value: int) -> None:
        bucket, i = self._index(key)
        if i >= 0:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket, i = self._index(key)
        if i < 0:
            return -1
        return bucket[i][1]

    def remove(self, key: int) -> None:
        bucket, i = self._index(key)
        if i >= 0:
            bucket.pop(i)
    
    def _hash(self, key):    # hash function
        return key % self.size

    def _index(self, key):
        hash_key = self._hash(key)
        bucket = self.buckets[hash_key]
        for i, (k, v) in enumerate(bucket): 
            if k == key:
                return bucket, i
        return bucket, -1
