class Solution:
    def gridGame(self, grid):
        # Manually compute prefix sums for both rows
        prefix_sums = [[0] * (len(grid[0]) + 1) for _ in range(2)]
        for r in range(2):
            for c in range(1, len(grid[0]) + 1):
                prefix_sums[r][c] = prefix_sums[r][c - 1] + grid[r][c - 1]

        result = float('inf')
        n = len(grid[0])

        # Evaluate the possible splits for robot 1 and robot 2
        for col in range(1, n + 1):
            # Points left for robot 2 if robot 1 goes through the top
            top_points = prefix_sums[0][n] - prefix_sums[0][col]
            # Points left for robot 2 if robot 1 goes through the bottom
            bottom_points = prefix_sums[1][col - 1]

            # Minimize the maximum points robot 2 can collect
            result = min(result, max(top_points, bottom_points))

        return result
