def longestPalindrome(s: str) -> int:
    freq_dict = defaultdict(int)
    for char in s:
        freq_dict[char] += 1

    res = 0
    odd_count_found = False
    for _, count in freq_dict.items():
        if count % 2 == 0:
            res += count
        else:
            res += count - 1
            odd_count_found = True

    return res + 1 if odd_count_found else res
