
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        Q = []  # Min-heap for storing queries
        store = [[] for _ in range(len(heights))] 
        # Create an empty list for each index to store queries
        res = [-1] * len(queries)  
        # Initialize the results array with -1 for all queries

        # Process each query and populate the store
        for k, (i, j) in enumerate(queries):
            if i == j:
                res[k] = i  # If both indices are the same, return the index
            elif i < j and heights[i] < heights[j]:
                res[k] = j  # If index i is less than j and height at i is less than at j, result is j
            elif j < i and heights[j] < heights[i]:
                res[k] = i  # If index j is less than i and height at j is less than at i, result is i
            else:
            # Store the query in the list for the index with the maximum height
                store[max(i, j)].append((max(heights[i], heights[j]), k))

        # Traverse each height in heights
        for i, h in enumerate(heights):
            # Maintain the heap property based on heights from heights array
            while Q and h > Q[0][0]:
                height, query_index = heapq.heappop(Q)
                res[query_index] = i  
    # Set the result for the query index to the current index

            # Push the current index's stored queries into the heap
            for s in store[i]:
                heapq.heappush(Q, s)

        return res
