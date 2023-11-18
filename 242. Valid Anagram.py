# sort 
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# dict
from collections import defaultdict
def isAnagram(s: str, t: str) -> bool:
    freq_dict = defaultdict(int)
    for char in s:
        freq_dict[char] += 1
    for char in t:
        freq_dict[char] -= 1
    return all(v == 0 for v in freq_dict.values())
