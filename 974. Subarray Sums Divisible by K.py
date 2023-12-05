def subarraysDivByK(nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    psumModK_dict = defaultdict(int)    
    psumModK_dict[0] = 1    
    res = 0

    for num in nums:
        psum += num
        psumModK = psum % k
        if psumModK in psumModK_dict:
            res += psumModK_dict[psumModK]
        psumModK_dict[psumModK] += 1

    return res
        
