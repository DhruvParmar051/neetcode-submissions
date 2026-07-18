class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j - i 
        #             break       
        # return res

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            
            stack.append(i)
        
        return res
        

