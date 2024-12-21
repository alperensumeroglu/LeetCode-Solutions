class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Q = deque([root])
        level = 0

        while Q:
            l = []
            for _ in range(len(Q)):
                node = Q.popleft()
                l.append(node)
                if node.left:
                    Q.append(node.left)
                    Q.append(node.right)

            if level & 1:  # Check if the level is odd
                left, right = 0, len(l) - 1
                while left < right:
                    l[left].val, l[right].val = l[right].val, l[left].val
                    left += 1
                    right -= 1

            level += 1

        return root