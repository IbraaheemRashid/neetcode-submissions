class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers
        # when sum is greater decrement, smaller increment

        l, r = 0, len(numbers)-1

        while l < r:
            sumN = numbers[l] + numbers[r]
            if sumN > target:
                r -= 1
            elif sumN < target:
                l += 1
            else:
                return [l+1, r+1]
