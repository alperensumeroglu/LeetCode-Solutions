class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = 0

        def dfs(cur, parent):
            nonlocal res
            total = values[cur]

            for child in adj[cur]:
                if child != parent:
                    total += dfs(child, cur)

            if total % k == 0:
                res += 1

            return total

        dfs(0, -1)
        return res

