class Solution:
    def minimumOperations(self, root: Optional['TreeNode']) -> int:
        q = deque([root])
        total = 0

        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            pos = {n: i for i, n in enumerate(sorted(row))}
            visited = set()

            for i in range(len(row)):
                index = i
                cnt = 0
                while index not in visited and pos[row[index]] != index:
                    visited.add(index)
                    index = pos[row[index]]
                    cnt += 1
                total += max(0, cnt - 1)

        return total