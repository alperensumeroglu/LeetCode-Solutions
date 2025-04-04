class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # -----------------------------
        # Intuition:
        # -----------------------------
        # The problem is to find the Lowest Common Ancestor (LCA) of the deepest leaves in a binary tree.
        # Deepest leaves are the nodes that are farthest from the root.
        # The LCA of these deepest leaves is the lowest node that has all the deepest leaves as descendants.

        # -----------------------------
        # Approach:
        # -----------------------------
        # Use a recursive post-order traversal.
        # For each node, we calculate the depth of its left and right subtrees.
        # - If both depths are equal, current node is the LCA.
        # - If left is deeper, recurse into left.
        # - If right is deeper, recurse into right.
        # Return a tuple of (LCA node, depth of subtree).

        def dfs(node, depth):
            if not node:
                # If node is None, return (None, current depth)
                return (None, depth)
            
            # Recursively traverse left and right children
            left_lca, left_depth = dfs(node.left, depth + 1)
            right_lca, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                # Left subtree is deeper → propagate its LCA and depth upward
                return (left_lca, left_depth)
            elif right_depth > left_depth:
                # Right subtree is deeper → propagate its LCA and depth upward
                return (right_lca, right_depth)
            else:
                # Both subtrees are at the same depth → current node is LCA
                return (node, left_depth)

        # Start recursive DFS from the root at depth 0
        lca_node, _ = dfs(root, 0)
        return lca_node

        # -----------------------------
        # Complexity:
        # -----------------------------
        # Time Complexity: O(N)
        #   - Each node is visited once → linear time with respect to number of nodes
        # Space Complexity: O(H)
        #   - H is the height of the tree → due to recursive stack space
        #   - Worst case (skewed tree) → O(N), Best case (balanced) → O(log N)
