# O(n*klogk)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)
    for word in strs:
        pattern = ''.join(sorted(word))  # sorted word as the key
        anagram_dict[pattern].append(word)

    return anagram_dict.values()
  
# O(nk)
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_dict = defaultdict(list)
    for word in strs:
        char_counts = [0] * 26
        for char in word:
            char_counts[ord(char) - ord('a')] += 1
        anagram_dict[tuple(char_counts)].append(word)  # char_count as the key

    return anagram_dict.values()
