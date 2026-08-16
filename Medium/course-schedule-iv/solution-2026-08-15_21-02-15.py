class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjList = defaultdict(list)
        for pre, crs in prerequisites:
            adjList[crs].append(pre)
        res = []
        preReqMap = {}

        def dfs(crs):
            if crs not in preReqMap:
                preReqMap[crs] = set()
                for c in adjList[crs]:
                    preReqMap[crs] |= dfs(c)
                preReqMap[crs].add(crs)
            return preReqMap[crs]

        for i in range(numCourses):
            dfs(i)
        
        for pre, crs in queries:
            res.append(pre in preReqMap[crs])
        
        return res