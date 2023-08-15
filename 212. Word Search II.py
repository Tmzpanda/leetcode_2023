def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie()
    for word in words:		
        trie.insert(word)

    def dfs(i, j, node, prefix):
        if node.is_word:
            res.append(prefix)
            trie.delete(prefix)     # optimize

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] in node.children:
                visited.add((x, y))
                dfs(x, y, node.children[board[x][y]], prefix+board[x][y])
                visited.remove((x, y))

    m, n = len(board), len(board[0])
    visited = set()
    res = []
    for i in range(m):
        for j in range(n):
            if board[i][j] in trie.root.children:
                visited.add((i, j))
                dfs(i, j, trie.root.children[board[i][j]], board[i][j])    
                visited.remove((i, j))        

    return list(set(res))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):	
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()  
            cur = cur.children[char]
        cur.is_word = True

    def delete(self, word):
        self._deleteTrieNode(self.root, word, 0)

    def _deleteTrieNode(self, node, word, index):
        if index == len(word):
            if node.is_word:
                node.is_word = False
            return
            
        char = word[index]
        if char not in node.children:
            return
        else:
            child_node = node.children[char]
            self._deleteTrieNode(child_node, word, index+1)

        if not child_node.children and not child_node.is_word:
            del node.children[char]

