class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            minLen = min(len(w1), len(w2))

            for j in range(minLen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
                
        visited = {}
        order = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True
        
            for nei in graph[char]:
                if dfs(nei):
                    return True
            
            visited[char] = False
            order.append(char)
            return False
        
        for char in graph:
            if dfs(char):
                return ""
            
        order.reverse()

        return "".join(order)