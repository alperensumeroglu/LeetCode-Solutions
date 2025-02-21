class FindElements:
    def __init__(self, root):
        """ 
        Initializes the object with a contaminated binary tree and recovers it.
        """
        self.values = set()
        self.recover_tree(root, 0)

    def recover_tree(self, node, value):
        """ 
        Recovers the binary tree by assigning correct values based on the given rules.
        """
        if not node:
            return
        node.val = value
        self.values.add(value)
        self.recover_tree(node.left, 2 * value + 1)
        self.recover_tree(node.right, 2 * value + 2)

    def find(self, target):
        """ 
        Returns True if the target value exists in the recovered binary tree, otherwise False.
        """
        return target in self.values

'''
# Intuition
The given tree is contaminated, meaning all values are initially set to -1.
We need to recover the tree by following the rules that determine the values of each node.
Once recovered, we should efficiently check whether a given target value exists in the tree.

# Approach
1. Use a recursive function to traverse and recover the tree.
2. Store all valid values in a set for quick lookup.
3. Implement the `find` method to check if a given target exists in the set.

# Complexity
- Time complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
- Space complexity: O(n), as we store the recovered values in a set.
'''