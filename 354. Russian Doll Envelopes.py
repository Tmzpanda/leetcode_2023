def maxEnvelopes(envelopes: List[List[int]]) -> int:
  
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    nums = [h for _, h in envelopes]
    return lengthOfLIS(nums)
