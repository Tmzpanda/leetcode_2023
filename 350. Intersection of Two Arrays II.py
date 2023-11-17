# freq_dict
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    freq_dict = defaultdict(int)
    for num in nums1:
        freq_dict[num] += 1
    
    res = []
    for num in nums2:
        if freq_dict[num] > 0:
            res.append(num)
            freq_dict[num] -= 1

    return res
