# two pointers
def minWindow(s: str, t: str) -> str:
    t_freq_dict = defaultdict(int)
    for c in t:
        t_freq_dict[c] += 1

    s_freq_dict = defaultdict(int)
    minLen = len(s) + 1
    window = ""
    matched = 0

    l = 0
    for r in range(len(s)):
        s_freq_dict[s[r]] += 1
        if s[r] in t_freq_dict and s_freq_dict[s[r]] == t_freq_dict[s[r]]:
            matched += 1
        
        while matched == len(t):    # shrink
            windowLen = r - l + 1
            if windowLen < minLen:
                minLen = windowLen
                window = s[l: r + 1]

            s_freq_dict[s[l]] -= 1
            if s[l] in t_freq_dict and s_freq_dict[s[l]] < t_freq_dict[s[l]]:
                    matched -= 1
            l += 1  

    return window
