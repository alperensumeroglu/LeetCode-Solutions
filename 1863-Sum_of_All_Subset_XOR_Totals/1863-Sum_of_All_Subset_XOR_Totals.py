class Solution:
    def subsetXORSum(self, nums):
        """
        Intuition:
        The task is to calculate the sum of XOR values of all subsets of the given list.
        XOR is a binary operation that outputs 1 if the bits are different.
        So for every subset, we compute the XOR of its elements and then sum up all of them.

        Approach:
        Use Depth-First Search (DFS) to recursively explore each subset.
        At each step, we make a binary decision: either include the current element or not.
        If we reach the end of the list, we have a complete subset and we add its XOR result.

        Complexity:
        Time: O(2^n) — We generate all possible subsets (2 choices per element).
        Space: O(n)  — Max depth of the recursive call stack.
        """

        self.result = 0  # Using self.result allows us to modify the variable across nested functions
                         # (nonlocal doesn't work here because we're inside a class method)

        def dfs(index, current_xor):
            """
            Recursive helper function to explore all subset combinations.

            Parameters:
            - index: The current index we are considering in the nums list.
            - current_xor: The XOR value accumulated so far from selected elements.

            Why use recursion?
            -> Because every element has 2 states: included or not included.
            -> This naturally forms a binary tree of decisions (2^n combinations).
            """

            # BASE CASE: If we've considered all elements, we've completed a subset.
            if index == len(nums):
                self.result += current_xor  # Add the XOR value of this complete subset to the result.
                return                      # No further elements to process, so return.

            # RECURSIVE CASE 1: Exclude the current element.
            # We don't change the XOR value because this number is not in the subset.
            dfs(index + 1, current_xor)

            # RECURSIVE CASE 2: Include the current element.
            # We XOR the current number with the current_xor to simulate inclusion.
            dfs(index + 1, current_xor ^ nums[index])

        # Start recursion from index 0 with initial XOR value of 0.
        # Why 0? Because 0 is the identity element for XOR (x ^ 0 = x).
        dfs(0, 0)

        # Finally, return the total XOR sum of all subsets.
        return self.result
# Keep coding and stay awesome! Your potential is LIMITLESS — just like the power of XOR!