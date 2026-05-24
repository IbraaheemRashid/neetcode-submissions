class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the array and try every combination
        # go through the array once, add everything to a dictionary
        # find the diff, if diff is in dictionary return i + diff

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return[seen[diff], i]
            seen[n] = i
        