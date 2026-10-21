class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we want to try one solution, chck if its the target, if we not
        # we can either go on one more or backtrack
        # we should backtrack if our currnt sum is greater than target
        # or if we have exhausted all options (but i dont think this is i possble given ewe csn use nums infinitely)

        path = []
        res = []

        def backtrack(start, total):
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, total + nums[i])
                path.pop()
            
        backtrack(0, 0)
        return res