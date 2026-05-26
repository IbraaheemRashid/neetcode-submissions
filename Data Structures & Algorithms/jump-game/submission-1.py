class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force is smth like, go to 1, check the value, increment by that much, if we get to a point where we cant 

        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
            
