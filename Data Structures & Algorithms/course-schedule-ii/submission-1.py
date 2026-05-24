class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {c: [] for c in range(numCourses)}

        visited = set()
        cycle = set()

        for crs, pre in prerequisites:
            prereqs[crs].append(pre)

        out = []

        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            
            cycle.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            
            visited.add(crs)
            cycle.remove(crs)
            out.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return out