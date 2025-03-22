class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        """
        Intuition:
        Count how many connected components in the undirected graph are complete (i.e., fully connected internally).
        A complete component with k nodes has exactly k*(k-1)/2 edges.

        Approach:
        1. Construct the graph using adjacency list.
        2. Traverse all nodes and for each unvisited node:
            - Use BFS to explore the full connected component.
            - Count the number of nodes and the number of edges inside the component.
            - Check if it's a complete graph using the formula.
        3. Also account for isolated nodes (they are trivially complete).
        4. Return the total count of complete components.

        Complexity:
        Time: O(N + E)
        Space: O(N + E)
        """

        # Adjacency list using collections.defaultdict without import
        adj = {}
        for i in range(n):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        complete_components = 0

        # Helper function to explore component and check completeness
        def is_complete_component(start_node):
            queue = [start_node]
            visited.add(start_node)
            nodes = [start_node]
            edge_count = 0

            while queue:
                current = queue.pop(0)
                for neighbor in adj[current]:
                    edge_count += 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        nodes.append(neighbor)

            node_count = len(nodes)
            actual_edges = edge_count // 2
            expected_edges = node_count * (node_count - 1) // 2
            return actual_edges == expected_edges

        # Traverse all nodes
        for i in range(n):
            if i not in visited:
                if not adj[i]:  # Isolated node
                    complete_components += 1
                elif is_complete_component(i):
                    complete_components += 1

        return complete_components

