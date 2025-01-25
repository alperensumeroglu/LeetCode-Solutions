class Solution:
    def eventualSafeNodes(self, graph):
        num_nodes = len(graph)
        queue = []  # To store terminal nodes or nodes with no outgoing edges
        reverse_graph = [[] for _ in range(num_nodes)]  # To store the reverse of the graph
        outdegree = [0] * num_nodes  # To track the number of outgoing edges for each node

        # Build the reverse graph and calculate the outdegree for each node
        for node in range(num_nodes):
            outdegree[node] = len(graph[node])
            if outdegree[node] == 0:  # If no outgoing edges, it's a terminal node
                queue.append(node)
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)

        safe_nodes = []  # List to store all eventual safe nodes

        # Process nodes with no outgoing edges and propagate their safeness
        while queue:
            current_node = queue.pop(0)
            safe_nodes.append(current_node)
            for parent in reverse_graph[current_node]:
                outdegree[parent] -= 1  # Remove the edge to the current node
                if outdegree[parent] == 0:  # If no outgoing edges remain, it's safe
                    queue.append(parent)

        return sorted(safe_nodes)  # Return the safe nodes in ascending order
