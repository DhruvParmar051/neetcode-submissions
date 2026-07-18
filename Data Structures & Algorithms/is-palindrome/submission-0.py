class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""

        for i in range(len(s)):
            if s[i].isalnum():
                s[i]
                st += s[i].lower()
        
        return st[::] == st[::-1]