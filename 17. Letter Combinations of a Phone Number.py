def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0: return []

    digToChar = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    n = len(digits)
    res = []

    def dfs(start, path):
        if len(path) == n:
            res.append("".join(path))
            return

        for char in digToChar[digits[start]]:
            path.append(char)
            dfs(start + 1, path)
            path.pop()

    dfs(0, [])
    return res
