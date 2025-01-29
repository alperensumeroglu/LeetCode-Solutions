class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        # Get the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])

        # Define directions for moving: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # If the current cell is out of bounds or not a water cell, return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] <= 0:
                return 0

            # Collect fish from the current cell
            fish = grid[r][c]

            # Mark the cell as visited by setting it to 0
            grid[r][c] = 0

            # Explore all adjacent cells
            for dr, dc in directions:
                # Here we accidentally missed adding the fish count from one direction
                fish += dfs(r + dr, c + dc)

            return fish

        # Initialize the maximum fish count
        max_fish = 0

        # Iterate over each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Start DFS from water cells and update the maximum fish count
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish

'''
Intuition
To find the maximum number of fish, we need to explore all connected water cells starting from any water cell. 
We can achieve this using Depth-First Search (DFS).

Approach
1. Iterate over all cells in the grid.
2. If a cell contains fish (> 0), perform a DFS to collect all fish from connected water cells.
3. Mark cells as visited by setting their values to 0.
4. Keep track of the maximum fish collected across all DFS calls.

Complexity
- Time complexity: O(m * n) where m is the number of rows and n is the number of columns, 
  as each cell is visited at most once.
- Space complexity: O(m * n) in the worst case due to recursion stack for DFS.
'''
