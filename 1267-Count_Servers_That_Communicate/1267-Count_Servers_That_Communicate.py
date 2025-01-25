class Solution:
    def countServers(self, grid):
        # Get the number of rows and columns in the grid
        rows_count = len(grid)
        cols_count = len(grid[0])

        # Initialize row and column counters to keep track of the number of servers
        row_servers = [0] * rows_count
        col_servers = [0] * cols_count

        # First pass: Count the number of servers in each row and column
        for row in range(rows_count):
            for col in range(cols_count):
                if grid[row][col] == 1:
                    row_servers[row] += 1
                    col_servers[col] += 1

        # Initialize the result variable
        communicating_servers = 0

        # Second pass: Count the servers that can communicate
        for row in range(rows_count):
            for col in range(cols_count):
                # A server can communicate if there are other servers in the same row or column
                if grid[row][col] == 1 and (row_servers[row] > 1 or col_servers[col] > 1):
                    communicating_servers += 1

        return communicating_servers