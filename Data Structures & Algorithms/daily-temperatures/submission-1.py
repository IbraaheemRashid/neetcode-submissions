class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # loop through temperatures
        # have a stack that we empty each time
        # add each non greater temp to the stack
        # append the length of the stack to res
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
        
        return res
                    