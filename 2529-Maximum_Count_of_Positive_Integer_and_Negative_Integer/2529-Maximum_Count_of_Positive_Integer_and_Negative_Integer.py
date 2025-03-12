class Solution:
    def maximumCount(self, nums):
        """
        Given a sorted array in non-decreasing order, return the maximum 
        count between the number of positive and negative integers.

        :param nums: List[int] - The input array.
        :return: int - The maximum count of either positive or negative numbers.
        """

        # Step 1: Initialize counters
        neg_count = 0
        n = len(nums)

        # Step 2: Iterate through the array to count negative numbers
        for i in range(n):
            if nums[i] == 0:
                continue  # Skip zeros since they are neither positive nor negative
            elif neg_count == 0 and nums[i] > 0:
                return n - i  # All remaining numbers are positive
            elif nums[i] < 0:
                neg_count += 1
            elif nums[i] > 0:
                return max(neg_count, n - i)  # Compare negative and positive counts
        
        # If only negative numbers exist or the list is empty
        return max(neg_count, 0)

"""
Intuition:
- The goal is to find the maximum count of positive or negative integers in a sorted array.
- Since the array is sorted, negative numbers appear first, followed by zeros (if any), and then positive numbers.

Approach:
1. Traverse the array while counting negative numbers.
2. If a positive number is encountered, compute the number of remaining positive numbers.
3. Return the maximum between the negative and positive counts.

Complexity:
- Time Complexity: O(n) in the worst case, but usually O(log n) if optimized with binary search.
- Space Complexity: O(1) since only a few integer variables are used.

🚀🔥 Keep coding and stay awesome!
"""
