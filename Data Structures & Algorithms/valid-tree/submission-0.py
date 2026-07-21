class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
    
        for u,v in edges:
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return False
            
            parent[pu] = pv
        
        return True
        