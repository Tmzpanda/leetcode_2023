BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
class Codec:
    def __init__(self):
        self.url_dict = {}
        self.num = 0
        self.alphabet = BASE62

    def encode(self, longUrl: str) -> str:
        # edge case
        if self.num == 0:
            shortUrl = self.alphabet[0]
            self.num += 1
            self.url_dict[shortUrl] = longUrl
            return shortUrl
        
        # convert decimal to BASE62
        arr = []
        base = len(self.alphabet)
        while quotient:
            quotient, remainder = divmod(self.num, base)    
            arr.append(alphabet[remainder])
        arr.reverse()
        shortUrl = ''.join(arr)
        self.url_dict[shortUrl] = longUrl
        self.num += 1
        
        return shortUrl
    
    def decode(self, shortUrl: str) -> str:
        return self.url_dict[shortUrl]
        
