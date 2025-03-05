class Solution:
    def coloredCells(self, n: int) -> int:
        # Initial number of colored cells (starting cell)
        total_cells = 1  

        # Iterating from the 2nd minute to n
        for i in range(2, n + 1):
            total_cells += (i - 1) * 4  # Each level adds 4 times the previous step

        return total_cells


"""
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

# Intuition
The problem follows a clear pattern of growth. At each minute, the number of new cells added 
is based on the previously colored cells, forming an expanding cross pattern.

# Approach
1. Start with one initially colored cell.
2. Every minute, four new cells are added for each existing boundary layer.
3. Using a loop from `2` to `n`, we increment the total count by `(i-1) * 4`, since the pattern
   grows symmetrically in all four directions.
4. Return the final count of colored cells.

# Complexity
• Time complexity: O(n), as we iterate linearly from 2 to n.
• Space complexity: O(1), since we use only a single integer variable.
"""
