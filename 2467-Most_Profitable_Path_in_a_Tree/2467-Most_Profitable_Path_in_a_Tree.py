class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        # Step 1: Construct adjacency list for an undirected tree
        adjacency_list = {}
        for u, v in edges:
            if u not in adjacency_list:
                adjacency_list[u] = []
            if v not in adjacency_list:
                adjacency_list[v] = []
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
        
        # Step 2: Find Bob's path to the root (node 0)
        bob_path = {}
        visited = set()

        def track_bob_path(node, time):
            """ Recursive function to track Bob's path to node 0 """
            visited.add(node)
            bob_path[node] = time
            if node == 0:
                return True
            for neighbor in adjacency_list[node]:
                if neighbor not in visited and track_bob_path(neighbor, time + 1):
                    return True
            bob_path.pop(node)
            return False

        track_bob_path(bob, 0)
        
        # Step 3: Perform DFS to determine the maximum profit for Alice
        visited.clear()
        max_profit = float('-inf')

        def explore_alice_path(node, time, income):
            """ DFS function to track Alice's path and compute the maximum profit """
            nonlocal max_profit
            visited.add(node)

            # Alice collects amount if Bob hasn't reached the node yet
            if node not in bob_path or time < bob_path[node]:
                income += amount[node]
            elif time == bob_path[node]:
                income += amount[node] // 2  # Bob and Alice split the amount

            # If the node is a leaf and not the root, check for maximum profit
            if len(adjacency_list[node]) == 1 and node != 0:
                max_profit = max(max_profit, income)

            # Continue DFS exploration
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    explore_alice_path(neighbor, time + 1, income)

        explore_alice_path(0, 0, 0)
        return max_profit

'''

🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

**Intuition**
Alice and Bob move through the tree, collecting amounts from nodes. The challenge is to determine the most profitable path Alice can take, considering that Bob might reach some nodes earlier and take part of the amount. 

**Approach**
1. Convert the given edges into an undirected adjacency list.
2. Find Bob's path to the root and store his arrival time at each node.
3. Use depth-first search (DFS) to track Alice’s movement while maximizing her collected amount.
4. If Bob arrives first, he takes the full amount; if they arrive at the same time, they split the amount.
5. The goal is to find the leaf node where Alice can collect the highest possible amount.

**Complexity**
• Time complexity: $$O(n)$$, as we traverse all nodes once.
• Space complexity: $$O(n)$$, due to adjacency list storage and recursion depth in DFS.

'''
