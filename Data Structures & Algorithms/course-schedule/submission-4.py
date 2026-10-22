class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # numCourses = 3, prerequisites = [[0,1],[1,0]]

        # we need to build an adjacency list to know which prereqs
        # we've seen
        # keep a visited set to make sure we don't keep visiting the 
        # same courses but also so if theres a cycle we can return -1

        # map each course to its pre

        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True