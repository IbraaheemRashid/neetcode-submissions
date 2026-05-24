class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through the array for each i and check if any of i + n is equal to i
        # real method is create a set, check if each integer is in the set, if not then add to the set

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False