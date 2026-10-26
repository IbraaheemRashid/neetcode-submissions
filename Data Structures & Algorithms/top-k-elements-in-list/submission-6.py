class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for i, num in enumerate(nums):
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            bucket[count].append(num)
        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res