def minimalKSum(nums: List[int], k: int) -> int:
    nums = list(set(nums))
    nums.sort()
    last = k
    substract_sum = 0
    for num in nums :
        if (num <= last) :  
            last += 1  
            substract_sum += num  
        else :
            break  

    return int((1+last)*last/2 - substract_sum)


def minimalKSum(nums: List[int], k: int) -> int:
      nums = sorted(set(nums))
      l, r = 0, len(nums)
      while l < r:
          mid = (l + r) // 2
          missing = nums[mid] - (mid+1)

          if missing < k:
              l = mid + 1
          else:
              r = mid

      s = l + k
      return s*(s+1)//2 - sum(nums[:l])
