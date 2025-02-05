class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        # Initialize variables for island ID and area mapping
        self.island_id = -1
        self.island_areas = {}

        # Directions for 4-connectivity: up, down, left, right
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Mark and calculate area for each island
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    island_area = self.dfs(grid, row, col)
                    self.island_areas[self.island_id] = island_area
                    self.island_id -= 1

        max_area = 0

        # Evaluate the effect of flipping each 0 to 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    area = 1
                    surrounding_islands = set()

                    for dr, dc in self.directions:
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] < 0:
                            surrounding_islands.add(grid[new_row][new_col])

                    # Add the areas of all connected islands
                    for island_id in surrounding_islands:
                        area += self.island_areas[island_id]

                    max_area = max(max_area, area)

        # If no flip is possible, return the area of the entire grid
        return max_area if max_area > 0 else len(grid) * len(grid[0])

    def dfs(self, grid: list[list[int]], row: int, col: int) -> int:
        # Base case: Out of bounds or not part of the island
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != 1:
            return 0

        # Mark the cell with the current island ID
        grid[row][col] = self.island_id

        # Initialize area as 1 for the current cell
        area = 1

        # Explore all 4 directions and calculate the total area
        for dr, dc in self.directions:
            area += self.dfs(grid, row + dr, col + dc)

        return area

"""
Intuition:
The problem is about finding the largest possible island after flipping one 0 to 1. Islands are groups of 1s connected 4-directionally.
By flipping a 0, we aim to merge neighboring islands, maximizing the connected area.

Approach:
1. Use DFS to identify islands and calculate their areas. Assign unique IDs to each island.
2. For each 0 in the grid, calculate the potential area of the island formed by flipping it to 1, considering all neighboring islands.
3. Keep track of the maximum area found.
4. Return the maximum area. If no flips are possible, return the total area of the grid.

Complexity:
- Time complexity: O(n^2), where n is the size of the grid. DFS traverses each cell once, and evaluating flips also involves examining all cells.
- Space complexity: O(n^2), for the recursive DFS stack and storing island areas.
"""
