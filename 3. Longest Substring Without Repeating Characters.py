def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    seen = set()
    res = 0

    start = 0
    for i in range(n):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[i])
        res = max(res, i - start + 1)

    return res
