class Solution:
    def maxArea(self, height: List[int]) -> int:
        mArea = 0
        left , right = 0 , len(height) -1

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            mArea = max(mArea, h * w)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return mArea 

        