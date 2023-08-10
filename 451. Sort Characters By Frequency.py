def frequencySort(s: str) -> str:
    charToFreq = defaultdict(int)
    res = ""

    for char in s:
        charToFreq[char] += 1
    items = sorted(charToFreq.items(), key=lambda item: -item[1])

    for char, freq in items:
        res += char*freq

    return res
