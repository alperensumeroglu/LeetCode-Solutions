class Solution:
    def goodTriplets(self, nums1, nums2):
        """
        Intuition:
        We want to count how many triplets (i < j < k) exist such that 
        nums1[i], nums1[j], nums1[k] appear in the same order in nums2.

        So, if we convert nums1 to the index order of nums2, the problem becomes:
        -> Count the number of increasing triplets in the new index list.

        Approach:
        - First, find out where each value in nums2 appears (its position).
        - Then, replace each value in nums1 with its index in nums2.
        - Now we want to count how many smaller elements are on the left
          and how many bigger elements are on the right for each index.
        - We do this using a Fenwick Tree (Binary Indexed Tree).

        Complexity:
        Time: O(n log n) because each update/query in Fenwick Tree takes log n time.
        Space: O(n) for extra arrays and the tree.
        """

        def update(tree, index, value):
            # Add 'value' to index in tree
            while index < len(tree):
                tree[index] += value
                index += index & -index  # Move to next responsible index

        def query(tree, index):
            # Get prefix sum from 1 to index
            result = 0
            while index > 0:
                result += tree[index]
                index -= index & -index  # Move to parent
            return result

        n = len(nums1)

        # Step 1: Create a map from number to its index in nums2
        # So we can know where each number is located in nums2
        position = {}
        for i in range(n):
            position[nums2[i]] = i

        # Step 2: Convert nums1 into positions from nums2
        # Now we just work with index values
        index_list = []
        for num in nums1:
            index_list.append(position[num])

        # Step 3: Count how many smaller values are to the left of each index
        # Fenwick Tree needs to be size n+2 because we work with 1-based index
        size = n + 2
        left_tree = [0] * size
        left_count = [0] * n

        for i in range(n):
            idx = index_list[i] + 1  # shift for 1-based BIT
            # Count of numbers smaller than current on the left
            left_count[i] = query(left_tree, idx - 1)
            update(left_tree, idx, 1)

        # Step 4: Count how many bigger values are to the right of each index
        right_tree = [0] * size
        right_count = [0] * n

        for i in range(n - 1, -1, -1):
            idx = index_list[i] + 1
            # Count of numbers bigger than current on the right
            right_count[i] = query(right_tree, n + 1) - query(right_tree, idx)
            update(right_tree, idx, 1)

        # Step 5: Multiply counts to get total number of good triplets
        total = 0
        for i in range(n):
            total += left_count[i] * right_count[i]

        return total
