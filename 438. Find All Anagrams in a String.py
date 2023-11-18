def findAnagrams(s: str, p: str) -> List[int]:
    p_freq_dict = defaultdict(int)
    s_freq_dict = defaultdict(int)
    for i in range(len(p)):
        p_freq_dict[p[i]] += 1
        s_freq_dict[s[i]] += 1

    res = [0] if s_freq_dict == p_freq_dict else []

    l = 0
    for r in range(len(p), len(s)):
        s_freq_dict[s[r]] += 1
        s_freq_dict[s[l]] -= 1
        if s_freq_dict[s[l]] == 0:
            s_freq_dict.pop(s[l])
        
        l += 1
        if s_freq_dict == p_freq_dict:
            res.append(l)

    return res

