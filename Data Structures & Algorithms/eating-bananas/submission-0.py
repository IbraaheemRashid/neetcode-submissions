class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know we can eat from 0 to the max[piles] bananas
        # so we do binary search and test, until we can eat every banana
        # in the time limit

        #[1,4,3,2] l = 0, r = 4, m = 2
        # go through list, add 1 hour until we get through all bananas
        # or until we reach h\

        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = (l+r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res