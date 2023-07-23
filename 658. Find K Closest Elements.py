def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
      n = len(arr)
      r = searchUpperClosest(arr, x)
      l = r - 1
  
      while r-l-1 < k:
          if l == -1:
              r += 1
              continue
          if r == n:
              l -= 1
              continue
          if x-arr[l] <= arr[r]-x:
              l -= 1
          else:
              r += 1
  
      return arr[l+1: r]
  
def searchUpperClosest(nums, target):
      l, r = 0, len(nums) - 1
      while l <= r:
          mid = (l + r) // 2
          if nums[mid] == target:
              return mid
          if nums[mid] < target:
              l = mid + 1
          else:
              r = mid - 1
      return l
