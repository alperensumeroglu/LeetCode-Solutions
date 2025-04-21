class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        Intuition:
        The problem is to determine how many valid starting values (within [lower, upper])
        can be used to build an array such that its consecutive differences match the given `differences` list.
        The array is implicitly defined by a starting point and applying these differences step by step.
        
        To ensure all elements of the constructed array stay within bounds, we track
        the cumulative min and max offset caused by the differences. Then we determine
        how many valid starting values (x) satisfy: lower <= x + offset <= upper for all offsets.

        Approach:
        1. Initialize the current sum (offset) as 0.
        2. For each difference in the array:
           - Update the cumulative sum.
           - Track the minimum and maximum cumulative sums.
        3. The valid starting value x must satisfy:
           lower <= x + min_offset  and  x + max_offset <= upper
           => x in [lower - min_offset, upper - max_offset]
        4. The total number of valid integers in that range is:
           max(0, upper - lower - max_offset + min_offset + 1)

        Complexity:
        Time Complexity: O(n) where n is the length of the `differences` list — single pass.
        Space Complexity: O(1) — only constant extra space is used.
        """

        # Initialize cumulative sum and track min/max deviations
        cumulative_sum = 0
        max_offset = 0
        min_offset = 0

        # Calculate running sum and track its min and max values
        for diff in differences:
            cumulative_sum += diff
            max_offset = max(max_offset, cumulative_sum)
            min_offset = min(min_offset, cumulative_sum)

        # Calculate number of valid starting values
        valid_range = (upper - lower) - (max_offset - min_offset) + 1

        # If the valid range is negative, return 0 (no valid array)
        return max(0, valid_range)

# 🚀🔥 Keep coding and stay awesome!
