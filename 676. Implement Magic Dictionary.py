class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()  
                cur = cur.children[char]
            cur.is_word = True

    def search(self, searchWord: str) -> bool:
        def dfs(i, cur, count):
            if i == len(searchWord):
                return cur.is_word and count == 1
            if count > 1:
                return False

            for char in cur.children:
                if dfs(i+1, cur.children[char], count+int(char!=searchWord[i])):
                    return True

            return False

        return dfs(0, self.root, 0)
