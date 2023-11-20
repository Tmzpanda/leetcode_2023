def partition(s: str) -> List[List[str]]:
    n = len(s)
    res = []
    def dfs(start, path):
        if start == n:
            res.append(list(path))
        for end in range(start, n):
            if isPalindrome(s[start: end+1]):
                path.append(s[start: end+1])
                dfs(end+1, path)
                path.pop()

    def isPalindrome(string):
        return string == string[::-1]

    dfs(0, [])
    return res
