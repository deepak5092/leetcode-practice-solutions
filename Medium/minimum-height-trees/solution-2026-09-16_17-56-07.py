class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        
        if n == 1:
            return [0]
        adj = defaultdict(list)
        dgrs = [0] * n
        q = deque()
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        for i in range(n):
            dgrs[i] = len(adj[i])
            if len(adj[i]) == 1:
                q.append(i)

        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                node = q.popleft()
                n -= 1
                for ch in adj[node]:
                    dgrs[ch] -= 1
                    if dgrs[ch] == 1:
                        q.append(ch)

        return list(q)