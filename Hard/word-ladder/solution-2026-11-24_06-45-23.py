from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # pattern dict
        patternDict = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patternDict[pattern].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                word = q.popleft()
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k+1:]
                    for nei in patternDict[pattern]:
                        if nei not in visit:
                            if nei == endWord:
                                return level + 1
                            visit.add(nei)
                            q.append(nei)

        return 0