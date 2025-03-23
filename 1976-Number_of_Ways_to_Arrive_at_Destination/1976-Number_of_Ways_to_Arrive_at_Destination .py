# ---------------------------------------------
# 🚀 1976. Number of Ways to Arrive at Destination
# ---------------------------------------------

# 💡 Intuition:
# We want to find the number of *different shortest paths* from node 0 to node (n - 1).
# This is a classic graph problem where we compute the shortest path using Dijkstra's algorithm,
# but we also count how many different ways we can reach each node using that minimum time.

# 🧭 Approach:
# 1. Build an adjacency list to represent the graph.
# 2. Use a modified Dijkstra algorithm:
#    - Track the shortest time to each node (time_to_node).
#    - Track the number of ways to reach each node using that shortest time (ways_to_node).
# 3. For each neighbor:
#    - If we found a shorter time, update both time and way count.
#    - If it's the same shortest time, increment the way count.
# 4. Return the number of ways to reach node (n - 1), modulo 1e9+7.

# ⏱️ Complexity:
# Time: O((N + E) * log N), where N is the number of nodes and E is the number of edges.
# Space: O(N + E), for the graph and auxiliary arrays.

class Solution:
    def countPaths(self, n, roads):
        # Initialize adjacency list for the graph
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))  # because roads are bidirectional

        # Initialize min-heap (priority queue): stores (travel_time, node)
        min_heap = [(0, 0)]

        # Shortest time to reach each node from source
        time_to_node = [float('inf')] * n
        time_to_node[0] = 0

        # Number of ways to reach each node with the shortest time
        ways_to_node = [0] * n
        ways_to_node[0] = 1

        MOD = int(1e9 + 7)

        while min_heap:
            # Pop the node with the smallest current travel time
            current_time, current_node = self.heappop(min_heap)

            for neighbor, travel_time in graph[current_node]:
                total_time = current_time + travel_time

                if total_time < time_to_node[neighbor]:
                    # Found a shorter path -> update
                    time_to_node[neighbor] = total_time
                    ways_to_node[neighbor] = ways_to_node[current_node]
                    self.heappush(min_heap, (total_time, neighbor))
                
                elif total_time == time_to_node[neighbor]:
                    # Found another shortest path -> add ways
                    ways_to_node[neighbor] = (ways_to_node[neighbor] + ways_to_node[current_node]) % MOD

        return ways_to_node[n - 1] % MOD

    # Custom heappush (min-heap insert)
    def heappush(self, heap, item):
        heap.append(item)
        self._siftup(heap, len(heap) - 1)

    # Custom heappop (min-heap extract min)
    def heappop(self, heap):
        last_item = heap.pop()
        if not heap:
            return last_item
        return_item = heap[0]
        heap[0] = last_item
        self._siftdown(heap, 0)
        return return_item

    # Maintain min-heap property after insert
    def _siftup(self, heap, pos):
        newitem = heap[pos]
        while pos > 0:
            parent = (pos - 1) >> 1
            if newitem < heap[parent]:
                heap[pos] = heap[parent]
                pos = parent
            else:
                break
        heap[pos] = newitem

    # Maintain min-heap property after remove
    def _siftdown(self, heap, pos):
        end_pos = len(heap)
        start_pos = pos
        newitem = heap[pos]
        child_pos = 2 * pos + 1
        while child_pos < end_pos:
            right_pos = child_pos + 1
            if right_pos < end_pos and heap[right_pos] < heap[child_pos]:
                child_pos = right_pos
            heap[pos] = heap[child_pos]
            pos = child_pos
            child_pos = 2 * pos + 1
        heap[pos] = newitem
        self._siftup(heap, pos)

# 🚀🔥 Keep coding and stay awesome!
