class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
        """
        This function solves the problem of finding the minimum cost walk 
        in a weighted graph, where the weight of the path is determined 
        by the bitwise AND of all the edges in the path.

        Parameters:
        - n: Number of nodes in the graph (0-indexed)
        - edges: List of edges where each edge is represented as [u, v, w] indicating
                 an edge between nodes u and v with a weight w.
        - queries: List of queries, where each query is a pair [s, t] representing
                   the start node s and the target node t for which we need to find 
                   the minimum cost walk.

        Returns:
        - A list of integers where each element corresponds to the minimum cost 
          of walking from s to t for each query. If no path exists, return -1 for that query.
        """
        
        # Step 1: Build the graph representation using adjacency list
        graph = {}
        for a, b, w in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, w))
            graph[b].append((a, w))

        # Step 2: Initialize dictionaries to track node clusters and their AND values
        n2c = {}  # Node to cluster_id mapping
        c2v = {}  # Cluster_id to bitwise-AND of all edges in the cluster

        # Step 3: Define BFS to explore the graph and assign nodes to clusters
        def bfs(node, cid):
            """
            Perform BFS starting from 'node' and assign all reachable nodes to the same cluster (cid).
            Also, compute the bitwise AND of all edges in the current cluster.
            """
            # Initialize the cluster's bitwise AND value to a very large value
            val = (1 << 17) - 1
            n2c[node] = cid  # Assign the node to the current cluster
            queue = [node]
            
            while queue:
                cur = queue.pop()
                if cur not in graph:
                    continue  # Skip if the node is not in the graph (avoid KeyError)
                for nb, w in graph[cur]:
                    val &= w  # Apply the bitwise AND for all edges in the cluster
                    if nb not in n2c:  # If the neighbor hasn't been visited yet
                        n2c[nb] = cid  # Assign the neighbor to the same cluster
                        queue.append(nb)  # Add the neighbor to the BFS queue
            
            # Store the final bitwise AND value for this cluster
            c2v[cid] = val

        # Step 4: Perform BFS on all unvisited nodes to form clusters
        cluster_id = 0
        for i in range(n):
            if i not in n2c:
                bfs(i, cluster_id)
                cluster_id += 1

        # Step 5: Answer the queries
        res = []
        for a, b in queries:
            if a == b:  # If the nodes are the same, cost is 0
                res.append(0)
            elif n2c[a] != n2c[b]:  # If the nodes are in different clusters, no path exists
                res.append(-1)
            else:  # If both nodes are in the same cluster, return the cluster's AND value
                res.append(c2v[n2c[a]])
        
        return res

# Explanation:
"""
Intuition:
The problem involves finding the minimum cost between two nodes in a graph. The cost is calculated by performing a bitwise AND operation on the weights of the edges encountered during the traversal. A node pair can only have a valid path if both nodes belong to the same connected component (cluster). If the nodes are in different clusters, no valid path exists.

Approach:
1. **Graph Representation**: The graph is represented as an adjacency list, where each node stores a list of tuples containing its neighbors and the associated edge weights.
2. **Cluster Assignment Using BFS**: We perform a BFS traversal from each unvisited node, assigning all reachable nodes to the same cluster. The bitwise AND of the edge weights is calculated during the BFS and stored for each cluster.
3. **Query Processing**: For each query, we simply check whether the two nodes belong to the same cluster. If they do, return the precomputed bitwise AND value for that cluster. If not, return -1.

Complexity:
- **Time Complexity**:
  - **Graph Construction**: O(m), where m is the number of edges.
  - **BFS Traversal**: O(n + m), where n is the number of nodes and m is the number of edges, as every node and edge is processed once.
  - **Query Processing**: O(q), where q is the number of queries, as we just check if two nodes belong to the same cluster and retrieve the corresponding AND value.
  
  Total time complexity: O(n + m + q), where n is the number of nodes, m is the number of edges, and q is the number of queries.

- **Space Complexity**:
  - **Graph Representation**: O(m) for storing the adjacency list.
  - **Cluster and AND values**: O(n) for storing the node-to-cluster mapping and the bitwise AND values for each cluster.
  
  Total space complexity: O(n + m).
"""

# 🚀🔥 Keep coding and stay awesome! You're on the right path to mastering graph algorithms!
