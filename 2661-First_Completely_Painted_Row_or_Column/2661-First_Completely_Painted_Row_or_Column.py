class Solution:
    def firstCompleteIndex(self, arr, mat):
        # Get dimensions of the matrix
        rows_count = len(mat)
        cols_count = len(mat[0])
        
        # Map each value in the matrix to its row and column indices
        value_to_position = {}
        for row in range(rows_count):
            for col in range(cols_count):
                value_to_position[mat[row][col]] = (row, col)
        
        # Track painted cells in each row and column using lists
        painted_rows = [0] * rows_count
        painted_cols = [0] * cols_count
        
        # Iterate over the paint sequence in arr
        for index, value in enumerate(arr):
            row, col = value_to_position[value]
            painted_rows[row] += 1
            painted_cols[col] += 1
            
            # Check if any row or column is fully painted
            if painted_rows[row] == cols_count or painted_cols[col] == rows_count:
                return index


