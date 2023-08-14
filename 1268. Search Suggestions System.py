def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    trie = Trie()
    for product in products:
        trie.insert(product)

    res = []
    prefix = ""
    for char in searchWord:
        prefix += char
        words = sorted(trie.startsWith(prefix))
        res.append(words[:3])

    return res


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()  
            cur = cur.children[char]
        cur.is_word = True
        
    def startsWith(self, prefix: str) -> List[str]:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return []
            cur = cur.children[char]
        
        words = []
        self._find_words_with_prefix(cur, prefix, words)
        return words
        
    def _find_words_with_prefix(self, node, current_word, words):
        if node.is_word:
            words.append(current_word)
        
        for char, child in node.children.items():
            self._find_words_with_prefix(child, current_word + char, words)
