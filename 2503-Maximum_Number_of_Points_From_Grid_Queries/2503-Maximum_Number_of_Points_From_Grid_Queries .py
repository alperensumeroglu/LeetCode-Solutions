class Solution:
    def maxPoints(self, grid, queries):
        """
        Calculate the maximum points for each query by traversing the grid starting from the top-left cell.
        Points are collected if the query value is strictly greater than the cell value, and cells are visited only once per query.
        
        Args:
            grid: The 2D grid representing cell values.
            queries: The list of query values.
            
        Returns:
            The list of maximum points for each query.
        """
        m, n = len(grid), len(grid[0])
        num_queries = len(queries)
        
        # Create a list of queries with their original indices for later reconstruction
        query_indices = [(queries[i], i) for i in range(num_queries)]
        # Sort the queries to process them in increasing order
        query_indices.sort()
        
        # Custom Min-Heap implementation
        class MinHeap:
            def __init__(self):
                self.heap = []
            
            def push(self, val):
                self.heap.append(val)
                self._sift_up(len(self.heap) - 1)
            
            def pop(self):
                if not self.heap:
                    return None
                self._swap(0, len(self.heap) - 1)
                val = self.heap.pop()
                self._sift_down(0)
                return val
            
            def _sift_up(self, idx):
                parent = (idx - 1) // 2
                if parent >= 0 and self.heap[parent][0] > self.heap[idx][0]:
                    self._swap(parent, idx)
                    self._sift_up(parent)
            
            def _sift_down(self, idx):
                left = 2 * idx + 1
                right = 2 * idx + 2
                smallest = idx
                if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
                    smallest = left
                if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
                    smallest = right
                if smallest != idx:
                    self._swap(smallest, idx)
                    self._sift_down(smallest)
            
            def _swap(self, i, j):
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            
            def peek(self):
                return self.heap[0] if self.heap else None
            
            def __len__(self):
                return len(self.heap)
        
        min_heap = MinHeap()
        min_heap.push((grid[0][0], 0, 0))
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[0][0] = True
        
        answer = [0] * num_queries
        total_points = 0
        
        # Process each query in sorted order
        for query, original_idx in query_indices:
            # Process all cells in the heap that are smaller than the current query
            while len(min_heap) > 0 and min_heap.peek()[0] < query:
                val, x, y = min_heap.pop()
                total_points += 1
                # Explore adjacent cells
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        min_heap.push((grid[nx][ny], nx, ny))
            # Assign the total points collected so far to the original query index
            answer[original_idx] = total_points
        
        return answer

# Intuition:
# The problem requires calculating the maximum points for each query, where points are earned by visiting cells
# with values strictly less than the query value. The challenge is to efficiently process multiple queries
# without reprocessing the grid from scratch for each query. By sorting the queries and using a min-heap,
# we can process cells in increasing order of their values, accumulating points as we go.

# Approach:
# 1. Sort the queries to process them in ascending order. This allows us to leverage the results from smaller
#    queries to answer larger ones efficiently.
# 2. Use a min-heap to always process the smallest unvisited cell next. This ensures that we handle cells
#    in the order of their values, which aligns with the sorted queries.
# 3. For each query, process all cells in the heap that are smaller than the query value, accumulate points,
#    and explore their adjacent cells if they haven't been visited yet.
# 4. Store the accumulated points for each query in the answer array at their original indices.

# Complexity:
# - Time Complexity: O(m * n log(m * n) + k log k), where m and n are the grid dimensions, and k is the number
#   of queries. The heap operations dominate the time complexity.
# - Space Complexity: O(m * n + k), for the heap, visited matrix, and storing the queries with their indices.

# Keep coding and conquer those algorithms like a pro! No imports needed this time! 