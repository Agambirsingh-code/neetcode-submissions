class Solution:
    def trap(self, height: List[int]) -> int:
        left =1 
        right = (len(height)-1)-1
        r = height[len(height)-1]
        l = height[0]
        water = 0
        while left <= right:
            if l <= r and height[left] < l:
                water += l-height[left]
                left +=1
            elif r <= l and height[right] < r:
                water += r-height[right]
                right -=1
            else:
                r = max(height[right], r)
                l = max(height[left], l)
                if r == height[right]:
                    right -= 1
                if l == height[left]:
                    left += 1

        return water