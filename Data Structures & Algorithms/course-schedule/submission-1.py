class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        # if there's a cycle then we know that its no good
        # creatge an adjacency list
        # check each course and its prerequisites, once we loop through all courses then we can return true
        # retgurn false at any point if we visit something that's in visited

        prereq = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if prereq[crs] == []:
                return True

            visited.add(crs)
            
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)

            prereq[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True