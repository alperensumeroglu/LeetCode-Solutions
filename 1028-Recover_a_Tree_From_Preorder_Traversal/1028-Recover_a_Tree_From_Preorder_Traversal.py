class Solution:
    def recoverFromPreorder(self, traversal: str):
        # Stack to keep track of nodes at different levels
        stack = []
        index, length = 0, len(traversal)

        while index < length:
            depth = 0

            # Count the number of dashes to determine depth
            while index < length and traversal[index] == '-':
                depth += 1
                index += 1

            # Read the numeric value of the node
            node_value = 0
            while index < length and traversal[index].isdigit():
                node_value = node_value * 10 + int(traversal[index])
                index += 1

            # Create a new node using LeetCode's TreeNode definition
            new_node = TreeNode(node_value)

            # Maintain stack depth and assign child nodes
            if len(stack) == depth:
                if stack:
                    stack[-1].left = new_node
            else:
                stack = stack[:depth]
                stack[-1].right = new_node

            # Append new node to stack
            stack.append(new_node)

        # Return root node
        return stack[0]

'''
Intuition
The input string represents a preorder traversal of a binary tree with depth information indicated by dashes. 
We need to reconstruct the tree structure based on this information.

Approach
1. Use a stack to keep track of nodes at different levels.
2. Iterate through the string to determine the depth of each node.
3. Extract the numeric value of the node.
4. If the stack size equals the depth, the node is a left child.
5. Otherwise, adjust the stack depth and assign the node as a right child.
6. Continue this process until all nodes are added.
7. Return the root node of the reconstructed tree.

Complexity
- Time complexity: O(n), where n is the length of the input string.
- Space complexity: O(n), since we use a stack to store tree nodes.
'''
