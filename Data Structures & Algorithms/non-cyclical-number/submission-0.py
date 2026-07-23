class Solution:
    def isHappy(self, n: int) -> bool:

        def digit_square_sum(n):
            res = 0 
            while n:
                digit = n % 10
                res += digit**2
                n //= 10
            return res
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)

        return n == 1 
