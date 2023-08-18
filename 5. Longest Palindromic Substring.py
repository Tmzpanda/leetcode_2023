def longestPalindrome(s: str) -> str:
    n = len(s)
    res = ""
    for i in range(n):
        s1 = getPalindrome(s, i, i) # odd
        s2 = getPalindrome(s, i, i+1) # even
        res = max([res, s1, s2], key=len)

    return res

def getPalindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1: r]
