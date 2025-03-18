class Solution:
    def longestNiceSubarray(self, nums):
        """
        Finds the length of the longest "nice" subarray.
        A subarray is "nice" if the bitwise AND of every pair of elements is zero.
        """

        # Intuition:
        # We need to find the longest contiguous subarray where every pair of elements has bitwise AND equal to zero.
        # Using a sliding window approach, we dynamically adjust the window size while maintaining the condition.

        # Approach:
        # 1. Use a sliding window with two pointers (left and right).
        # 2. Maintain a bitmask to keep track of the bitwise OR of elements in the window.
        # 3. Expand the right pointer, adding new elements while maintaining the "nice" condition.
        # 4. If adding an element violates the condition, shrink the left pointer until it's restored.
        # 5. Track the maximum window size found.

        left = 0  # Left boundary of the window
        bitmask = 0  # Stores the OR of all numbers in the window
        max_length = 0  # Tracks the longest valid subarray

        for right in range(len(nums)):
            # If adding nums[right] breaks the condition, move left pointer
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove nums[left] from bitmask
                left += 1  # Shrink the window from the left

            # Add the new element to the bitmask
            bitmask |= nums[right]

            # Update max_length if the current window is larger
            max_length = max(max_length, right - left + 1)

        # Complexity:
        # - Each number is added and removed from the bitmask at most once.
        # - Time Complexity: O(N), where N is the length of nums (linear time).
        # - Space Complexity: O(1), since only a few integer variables are used.

        return max_length

# 🚀🔥 Keep coding and stay awesome!
