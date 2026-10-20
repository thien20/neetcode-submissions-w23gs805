class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns = {}
        for word in wordList:
            for i in range(len(beginWord)):
                current = word[:i] + "*" + word[i+1:]
                if current not in patterns:
                    patterns[current] = []
                patterns[current].append(word)
        
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(beginWord)):
                current = word[:i] + "*" + word[i+1:] 
                for neighbor in patterns.get(current, []):
                    if neighbor in visited:
                        continue
                    queue.append((neighbor, step+1))
                    visited.add(neighbor)

        return 0
