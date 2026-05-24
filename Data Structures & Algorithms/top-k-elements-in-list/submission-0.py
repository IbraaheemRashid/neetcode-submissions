class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we create an array res of size nums
        # we loop through nums, creating a hashmap for each occurence
        # we append to res list the num depending on number of occurence
        # after we've looped through, we work from the end of the array backwards
        # till we get top k

        count = [[] for i in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for num, cnt in freq.items():
            count[cnt].append(num)
        
        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res