class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an array of length nums
        # loop through nums, add its count to a hashamp
        # after loop through the hasmpa and add to the index(frequency) the numbers

        # after we loop from the end till we get top k

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res