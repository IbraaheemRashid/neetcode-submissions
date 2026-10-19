class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get the middle
        # find if middle is greater or equal to target
        # if bigger than mvoe right pointer to middle - 1
        # else smaller move left pointer to middle + 1
        # else we have target and can return the index
        # 

        l, r = 0, len(nums) - 1

        while l <= r:
            middle = l +(( r-l) // 2)

            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle
        
        return -1