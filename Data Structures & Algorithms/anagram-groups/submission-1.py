class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we group if characters are all equal
        # we can have a char list that we update 
        # have a charlist hashmap, add each and then just loop and get each value in that hashmap

        res = defaultdict(list)

        for st in strs:
            chars = [0] * 26
            for char in st:
                chars[ord(char) - ord('a')] += 1
            res[tuple(chars)].append(st)
        return list(res.values())