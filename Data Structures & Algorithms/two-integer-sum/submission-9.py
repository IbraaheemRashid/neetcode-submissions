class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have a hashmap where the key is the num and the value is the index (or other wayu)

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i
        
