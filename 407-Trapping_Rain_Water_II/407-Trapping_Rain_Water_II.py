# 407-Trapping_Rain_Water_II.py

class Solution:
    def trapRainWater(self, heightMap):
        # Check if the heightMap is valid
        if not heightMap or not heightMap[0]:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = []  # Custom heap implementation (min-heap)
        water_trapped = 0

        # Custom function to push into the heap
        def heap_push(heap, value):
            heap.append(value)
            idx = len(heap) - 1
            while idx > 0:
                parent = (idx - 1) // 2
                if heap[parent][0] > heap[idx][0]:
                    heap[parent], heap[idx] = heap[idx], heap[parent]
                    idx = parent
                else:
                    break

        # Custom function to pop from the heap
        def heap_pop(heap):
            if not heap:
                return None
            value = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            idx = 0
            while True:
                left = 2 * idx + 1
                right = 2 * idx + 2
                smallest = idx
                if left < len(heap) and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < len(heap) and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest != idx:
                    heap[smallest], heap[idx] = heap[idx], heap[smallest]
                    idx = smallest
                else:
                    break
            return value

        # Add all boundary cells to the heap
        for r in range(rows):
            for c in [0, cols - 1]:  # First and last column
                heap_push(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(cols):
            for r in [0, rows - 1]:  # First and last row
                heap_push(heap, (heightMap[r][c], r, c))
                visited[r][c] = True

        # Directions for traversing neighbors (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Process cells in the heap
        while heap:
            height, x, y = heap_pop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within bounds and not visited
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    # Water is trapped if the current height is greater than the neighbor's height
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Add the neighbor to the heap with the max height
                    heap_push(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return water_trapped
