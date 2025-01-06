class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Variable to store the result
        unique_palindromes = 0
        # Find all unique characters in the string
        unique_chars = set(s)
        
        for char in unique_chars:
            # Find the first and last occurrence of the character
            first_index = s.find(char)  # Search from the beginning
            last_index = s.rfind(char) # Search from the end
            
            # Check if there is a valid range between the first and last occurrence
            if first_index < last_index:
                # Add the count of unique characters between the first and last index
                unique_palindromes += len(set(s[first_index + 1:last_index]))
        
        return unique_palindromes
