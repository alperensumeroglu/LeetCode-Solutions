from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def backtrack(index: int) -> bool:
            # If we have filled all positions, return True
            if index == size:
                return True
            
            # If the current position is already filled, move to the next one
            if result[index] != 0:
                return backtrack(index + 1)
            
            # Try placing numbers from n down to 1 for lexicographically largest sequence
            for num in range(n, 0, -1):
                if num == 1:
                    # Place '1' if it has not been used
                    if num not in used:
                        result[index] = 1
                        used.add(num)
                        
                        if backtrack(index + 1):
                            return True
                        
                        # Backtrack
                        result[index] = 0
                        used.remove(num)
                else:
                    # Place 'num' only if both required positions are available
                    if num not in used and index + num < size and result[index + num] == 0:
                        result[index] = result[index + num] = num
                        used.add(num)
                        
                        if backtrack(index + 1):
                            return True
                        
                        # Backtrack
                        result[index] = result[index + num] = 0
                        used.remove(num)
            
            return False
        
        # Initialize required structures
        used = set()
        size = 1 + (n - 1) * 2
        result = [0] * size
        
        # Start backtracking
        backtrack(0)
        
        return result
"""
# Intuition
To construct the lexicographically largest valid sequence, we need to place numbers from `n` to `1` such that:
- Each number `x` (except `1`) appears twice in the sequence with exactly `x` positions apart.
- The number `1` appears once.

We use backtracking to explore possibilities while ensuring the largest numbers are placed first.

# Approach
1. Use a backtracking approach to construct the sequence step by step.
2. Maintain a `set` to track used numbers.
3. Start placing numbers from `n` to `1` to ensure lexicographical order.
4. If a number `x > 1` is placed at `i`, then it must also be placed at `i + x`.
5. If a valid sequence is found, return it; otherwise, backtrack and try different possibilities.

# Complexity
- Time complexity: $$O(n!)$$ in the worst case due to backtracking, though pruning helps reduce it.
- Space complexity: $$O(n)$$ for maintaining the `used` set and recursion depth.
"""