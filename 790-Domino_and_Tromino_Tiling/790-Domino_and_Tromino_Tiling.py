class Solution:
    # The function numTilings calculates the number of ways to tile a 2xN board using 1x2 dominos and 2x1 dominoes
    # with the result modulo 10^9 + 7 to avoid overflow.
    
    def numTilings(self, n: int) -> int:
        # Base case for small values of n (1, 2, 3) which are pre-calculated.
        base_cases = (1, 1, 2)
        
        # Dictionary to store previously computed results (memoization)
        memo = {}

        def f(n):
            # If the result for n is already computed, return it from memo
            if n in memo:
                return memo[n]
            
            # If n is less than 3, return the pre-calculated base case values.
            if n < 3:
                return base_cases[n]
            
            # Recursive case: for n >= 3, the number of ways to tile a 2xN board is:
            # 2 * f(n-1) + f(n-3)
            # This equation comes from considering two possibilities:
            # 1. A vertical tile placed at the end, which leaves us with a 2x(n-1) board.
            # 2. A 2x2 square tile placed at the end, which leaves us with a 2x(n-3) board.
            result = (2 * f(n-1) + f(n-3)) % (10**9 + 7)
            
            # Store the result in the memo dictionary to avoid redundant calculations
            memo[n] = result
            
            return result
        
        # Return the result for the given n
        return f(n)

# The following are the explanations for the problem, approach, and time complexity:

# Intuition:
# The problem is about tiling a 2xN board using 1x2 and 2x1 dominos. The task is to count how many ways we can do this.
# We can break down the problem into smaller subproblems, by considering how we might fill the last part of the board.
# The recurrence relation (f(n) = 2 * f(n-1) + f(n-3)) comes from these choices, which is solved efficiently using dynamic programming.

# Approach:
# 1. The base cases are pre-calculated: for n = 0, 1, and 2, we already know the number of ways to tile the board.
# 2. For larger n, we use dynamic programming to recursively calculate the number of ways to tile a 2xN board:
#    - If we place a vertical domino, the problem reduces to tiling a 2x(n-1) board.
#    - If we place a 2x2 square domino, the problem reduces to tiling a 2x(n-3) board.
# 3. We use a dictionary `memo` to store intermediate results and avoid redundant calculations.
# 4. Finally, we return the result for the given n, modulo 10^9 + 7 to handle large numbers.

# Complexity:
# Time Complexity: O(n), because the function f(n) is computed only once for each value of n using memoization.
# Space Complexity: O(n), due to the space used by the memo dictionary to store intermediate results.

# 🚀🔥 Keep coding and stay awesome! 💪
