class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> str:
            while (l >= 0 and r < len(s) and 
                   s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        result = ""
        for i in range(len(s)):
            # For palindromes with odd length
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
                
            # For palindromes with even length
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
                
        return result