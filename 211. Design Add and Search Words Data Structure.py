class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()  
            cur = cur.children[char]
        cur.is_word = True
        
    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.is_word
            
            if word[i] != '.':
                if word[i] not in cur.children:
                    return False
                return dfs(i+1, cur.children[word[i]])
            else:
                for node in cur.children.values():
                    if dfs(i+1, node):
                        return True
                return False
        
        return dfs(0, self.root)
      
