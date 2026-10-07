class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap with count
        # array of lenth nums with [] in each slot
        # go through hashmap and append to relevant slot
        # work backwards throught the array until res is of length k

        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
