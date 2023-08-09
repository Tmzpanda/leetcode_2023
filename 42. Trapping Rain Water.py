"""
   input  [0,1,0,2,1,0,1,3,2,1,2,1]
 maxLeft  [0,0,1,1,2,2,2,2,3,3,3,3]  ->
maxRight  [3,3,3,3,3,3,3,2,2,2,1,0]  <-
min(L,R)  [0,0,1,1,2,2,2,2,2,2,1,0]
    trap  [0,0,1,0,1,2,1,0,0,1,0,0]  min(L,R)-input 
        
"""

def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res
