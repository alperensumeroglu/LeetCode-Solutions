class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        # Memoization dictionary
        memo = {}
        
        def dfs(length):
            # If length already computed, return it
            if length in memo:
                return memo[length]
            # If length exceeds the upper bound, no valid strings
            if length > high:
                return 0
            
            # Base count: If length is within bounds, count it as 1
            count = 1 if low <= length <= high else 0
            
            # Add strings formed by adding 'zero' or 'one'
            count += dfs(length + zero)
            count += dfs(length + one)
            
            # Store the result modulo MOD
            memo[length] = count % MOD
            return memo[length]
        
        # Start DFS from length 0
        return dfs(0)
