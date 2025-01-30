
class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Represent the graph as an adjacency list
        # Initialize an empty adjacency list for n nodes
        graph = [[] for _ in range(n)]
        for u, v in edges:
            u -= 1  # Convert to 0-based indexing
            v -= 1
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Check if the graph is bipartite
        # Initialize a list to store the color of each node (-1 indicates unvisited)
        colors = [-1] * n

        # Define a helper function for DFS-based bipartite check
        def is_bipartite(node, color):
            colors[node] = color  # Assign the current color to the node
            for neighbor in graph[node]:
                if colors[neighbor] == -1:  # If the neighbor is unvisited
                    if not is_bipartite(neighbor, 1 - color):  # Recur with alternate color
                        return False
                elif colors[neighbor] == color:  # If the neighbor has the same color
                    return False  # Graph is not bipartite
            return True

        # Check bipartite condition for all connected components
        for i in range(n):
            if colors[i] == -1:  # If the node is unvisited
                if not is_bipartite(i, 0):  # Start DFS with color 0
                    return -1  # Return -1 if the graph is not bipartite

        # Step 3: Calculate the maximum depth for each connected component
        # Define a helper function to calculate the maximum depth using BFS
        def bfs_max_depth(node):
            queue = [node]  # Initialize the queue for BFS
            visited = {node: 1}  # Store the depth of each node
            max_depth = 1  # Track the maximum depth

            while queue:
                current = queue.pop(0)  # Dequeue the current node
                for neighbor in graph[current]:
                    if neighbor not in visited:  # If the neighbor is unvisited
                        visited[neighbor] = visited[current] + 1  # Update its depth
                        max_depth = max(max_depth, visited[neighbor])  # Update max depth
                        queue.append(neighbor)  # Enqueue the neighbor
            return max_depth

        # Initialize variables for the final result
        visited = [False] * n  # Track visited nodes for connected components
        total_groups = 0  # Count of total groups

        # Define a DFS function to process each connected component
        def dfs(node):
            visited[node] = True  # Mark the node as visited
            max_group = bfs_max_depth(node)  # Get the maximum depth for this component
            for neighbor in graph[node]:
                if not visited[neighbor]:  # If the neighbor is unvisited
                    max_group = max(max_group, dfs(neighbor))  # Recur for the neighbor
            return max_group

        # Process all nodes to calculate the total groups
        for i in range(n):
            if not visited[i]:  # If the node is unvisited
                total_groups += dfs(i)  # Process the connected component

        return total_groups

'''
# Intuition
The problem is essentially about grouping nodes in such a way that adjacency constraints are met. To achieve this:
1. The graph needs to be bipartite, meaning nodes can be colored with two colors without conflicts.
2. Within each connected component, the maximum number of groups corresponds to the maximum depth of the graph when traversed.

# Approach
1. **Graph Representation**:
   - Represent the graph as an adjacency list to allow efficient traversal.
2. **Bipartite Check**:
   - Use a DFS-based algorithm to check if the graph is bipartite. This ensures that the adjacency constraints can be satisfied.
3. **Depth Calculation**:
   - Use a BFS-based algorithm to calculate the maximum depth of each connected component, which corresponds to the number of groups.
4. **Combine Results**:
   - Traverse all nodes and sum up the maximum depths for all connected components.

# Complexity
- Time complexity: $$O(n + e)$$, where $$n$$ is the number of nodes and $$e$$ is the number of edges. This accounts for the bipartite check and BFS traversals.
- Space complexity: $$O(n + e)$$ for storing the graph and auxiliary data structures.

'''