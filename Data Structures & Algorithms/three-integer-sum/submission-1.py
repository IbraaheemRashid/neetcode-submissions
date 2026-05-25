class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop through the array, get left and right being i + 1 and len(nums)
        # sort the array, increment i or 

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[i] + nums[l] + nums[r] <= 0:
                    l += 1
                else:
                    r -= 1
        
        return res
