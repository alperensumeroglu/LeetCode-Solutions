class Solution:
    def numberOfSubstrings(self, s: str) -> int:  
        # Dictionary to keep track of character counts in the current window
        char_count = {"a": 0, "b": 0, "c": 0}  
        
        i = 0  # Left pointer
        j = 0  # Right pointer
        total_substrings = 0  
        n = len(s)  
        
        while j < n:  
            # Expand the window by including the current character
            char_count[s[j]] += 1  
            j += 1  

            # When all characters 'a', 'b', and 'c' are present in the window
            while all(char_count[c] > 0 for c in "abc"):  
                # Count all substrings starting from 'i' to 'n'
                total_substrings += n - j + 1  
                
                # Shrink the window from the left
                char_count[s[i]] -= 1  
                i += 1  
        
        return total_substrings  

"""
        Intuition:
        ------------
        - We need to count the number of substrings that contain at least one 'a', 'b', and 'c'.
        - Instead of generating all possible substrings (which is inefficient), we use the **Sliding Window** technique.
        - The key idea is to expand the window until it contains at least one of each character, then move the left pointer 
        to explore all valid substrings.w

        Approach:
        ------------
        1. Use two pointers (i and j) to create a dynamic window.
        2. Expand `j` until the window contains at least one 'a', 'b', and 'c'.
        3. Once valid, every substring starting from `i` to `n` is valid.
        4. Move `i` forward to look for other valid substrings while maintaining the constraint.
        5. Repeat until all substrings are explored.

        Complexity:
        ------------
        - Time Complexity: **O(n)** → Each character is processed at most twice (once for expanding, once for shrinking).
        - Space Complexity: **O(1)** → We only store counts for 'a', 'b', and 'c'.
        """