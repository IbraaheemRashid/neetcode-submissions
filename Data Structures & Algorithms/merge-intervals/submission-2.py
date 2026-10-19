class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # what consistutes merging
        # in this case, if the start of the next sorted interval < 
        # the end of the current

        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        res = []

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                res.append(prev)
                prev = interval
        
        res.append(prev)
        
        return res