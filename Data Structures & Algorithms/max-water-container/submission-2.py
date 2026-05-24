class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, one at each end
        # check the area, if the area is larger than the current max, set to max
        # if not, then check the smallest of left and right and increment / decrement
        # once l == r, end the loop

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                l += 1
        
        return maxArea

