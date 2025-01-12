class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Create a dictionary to store the frequency of each character
        char_count = {}
        
        # Count the frequency of each character in the string
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Initialize a variable to track how many characters have an odd frequency
        odd_count = 0
        
        # Iterate over the frequency of characters
        for count in char_count.values():
            # Check if the frequency of the character is odd
            if count % 2 == 1:
                odd_count += 1
        
        # If the number of required palindromes k is greater than or equal to 
        # the odd frequency count and k is less than or equal to the length of the string
        if k >= odd_count and k <= len(s):
            return True
        
        return False
