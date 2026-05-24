class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what dictates a valid tree, im assuming that a cycle makes it invalid
        # do depth first, keep a track of visited, if we see a visited one more than once, just return False
        # otherwise if we get back only good responses, return True!

        if len(edges) >= n:
            return False
        
        adj = [[] for i in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True
        
        return dfs(0, -1 ) and len(visited) == n