class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        q = deque([(beginWord,1)])                
    
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps 
            
            word = list(word)

            for i in range(len(word)):
                original = word[i]

                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == original:
                        continue
                    
                    word[i] = ch
                    newWord = "".join(word)

                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        q.append((newWord,steps+1))
                
                word[i] = original
    
        return 0