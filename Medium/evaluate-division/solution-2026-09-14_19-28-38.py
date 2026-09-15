class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list)
        res = []

        for i in range(len(equations)):
            n, d = equations[i]
            val = values[i]
            adj[n].append([d, val])
            adj[d].append([n, 1 / val])
        
        def dfs(cur, target, path):
            if cur == target:
                return 1.00
            
            path.add(cur)

            for nei, wei in adj[cur]:
                if nei not in path:
                    query_res = dfs(nei, target, path)
                    if query_res != -1:
                        return query_res * wei 

            return -1.0000

        for qn, qd in queries:
            if qn not in adj or qd not in adj:
                res.append(-1.0000)
                continue
            res.append(dfs(qn, qd, set()))
        
        return res