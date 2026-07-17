class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            group[tuple(sorted(word))].append(word)
        
        res = []

        for key, value in group.items():
            print(key, value)
            res.append(value)
        
        return res