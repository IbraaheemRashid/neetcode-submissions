class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # hashmap mapping all prereqs to each course
        # then we want to go through each course, if we've already run dfs on it then return True
        # otherwise run dfs on all the prereqs, ideally should return True, if we see a course
        # we've already seen, then it's a cycle so not possible so empty array

        prereqs = {c: [] for c in range(numCourses)}
        for crs, prereq in prerequisites:
            prereqs[crs].append(prereq)

        visited, visiting = set(), set()
        output = []
        
        def dfs(crs):
            if crs in visited:
                return True
            if crs in visiting:
                return False
            
            visiting.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            
            visited.add(crs)
            output.append(crs)
            
            visiting.remove(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output