# sort 
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# dict
from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    charToFreq = defaultdict(int)
    for char in s:
        charToFreq[char] += 1
    for char in t:
        charToFreq[char] -= 1
    return all(v == 0 for v in charToFreq.values())
