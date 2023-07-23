def subarraySum(nums: List[int], k: int) -> int:
    psum = 0
    psum_dict = defaultdict(int)
    psum_dict[0] = 1
    res = 0
    for num in nums: 
        psum += num
        if psum - k in psum_dict:
            res += psum_dict[psum - k]
        psum_dict[psum] += 1
    
    return res
            
