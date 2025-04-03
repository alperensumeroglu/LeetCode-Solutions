class Solution:
    def maximumTripletValue(self, nums):
        """
        Intuition:
        We need to find the maximum value of the expression:
            (nums[i] - nums[j]) * nums[k], where i < j < k
        Instead of checking all triplets (which would be O(n^3)),
        we restructure the logic:
            Let 'middle' be nums[j]
            Let 'left' be the maximum value before j
            Let 'right' be the maximum value after j
        Then the expression becomes:
            (left - middle) * right
        Our goal is to find the maximum such value for all valid j.

        Approach:
        1. Traverse from left to right and build `left_max[i]` as the maximum of nums[0..i]
        2. Traverse from right to left and build `right_max[i]` as the maximum of nums[i..n-1]
        3. For each index j from 1 to n-2 (as j must be in the middle), calculate:
            (left_max[j-1] - nums[j]) * right_max[j+1]
           and keep track of the maximum result.

        Complexity:
        - Time Complexity: O(n) - 3 linear scans
        - Space Complexity: O(n) - two extra arrays of size n
        """

        n = len(nums)
        if n < 3:
            return 0  # Cannot form a triplet if fewer than 3 elements

        # Step 1: Build prefix max array
        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        # Step 2: Build suffix max array
        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        # Step 3: Evaluate the expression for valid middle indices
        max_triplet_value = 0
        for j in range(1, n - 1):
            left = left_max[j - 1]
            middle = nums[j]
            right = right_max[j + 1]
            current_value = (left - middle) * right
            max_triplet_value = max(max_triplet_value, current_value)

        return max_triplet_value

# 🚀🔥 Keep coding and stay awesome! You're leveling up like a pro!
