class TwoSum:
    def __init__(self):
        self.freq_dict = defaultdict(int)
        
    def add(self, number: int) -> None:
        self.freq_dict[number] += 1
        

    def find(self, value: int) -> bool:
        for num in self.freq_dict:
            complement = value - num
            if complement in self.freq_dict:    
                if complement != num or self.freq_dict[num] > 1:
                    return True

        return False
