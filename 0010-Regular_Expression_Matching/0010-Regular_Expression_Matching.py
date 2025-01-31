class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Using a dictionary to store computed results for memoization
        memo = {}
        
        # Define a helper function for Depth-First Search (DFS) with memoization
        def dfs(i, j):
            # Check if the result is already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we've reached the end of both strings, it's a match
            if i >= len(s) and j >= len(p):
                return True
            
            # If we've reached the end of the pattern but not the string, no match
            if j >= len(p):
                return False
            
            # Check if the current characters match or if the pattern has a '.'
            current_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Handle '*' in the pattern
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Either skip the '*' and its preceding character or use it if it matches
                memo[(i, j)] = dfs(i, j + 2) or (current_match and dfs(i + 1, j))
                return memo[(i, j)]
            
            # If current characters match, move to the next characters in both strings
            if current_match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            # If no match, store and return False
            memo[(i, j)] = False
            return False
        
        # Start the recursion
        return dfs(0, 0)

'''

# Intuition
The problem can be approached using recursion to simulate the matching process. We use memoization to store results of already computed states to optimize and avoid redundant calculations.

# Approach
1. Use Depth-First Search (DFS) to recursively check character matches between the input string `s` and the pattern `p`.
2. Handle two cases for the '*' character:
   - Skip the '*' and the preceding character entirely.
   - Use the '*' if the preceding character matches the current character in the string.
3. Use a dictionary for memoization to store results of already visited states `(i, j)`.
4. If the current characters match (or the pattern has a '.'), move to the next characters in both strings.
5. Return True only if all characters in both the string and the pattern are matched.

# Complexity
- Time complexity: O(n * m), where n is the length of the string `s` and m is the length of the pattern `p`. Each state `(i, j)` is visited at most once.
- Space complexity: O(n * m) due to the recursion stack and memoization table.
'''