class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        def children(code):
            res = []
            for i in range(4):
                num = int(code[i])
                dig = str((num + 1) % 10) 
                res.append(code[:i] + dig + code[i+1:])
                dig = str((num - 1 + 10) % 10) 
                res.append(code[:i] + dig + code[i+1:])
            return res 

        q = deque([("0000", 0)])
        visit = set(deadends)

        while q:

            lock, turns = q.popleft()

            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])

        return -1        