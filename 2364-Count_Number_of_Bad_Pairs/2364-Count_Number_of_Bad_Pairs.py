class Solution:
    def countBadPairs(self, nums):
        n = len(nums)  # Get the length of the array
        freq_map = {}  # Initialize a frequency map to count differences
        bad_pairs = 0  # Initialize the counter for bad pairs

        for j in range(n):
            # Calculate the difference for the current index
            diff = nums[j] - j
            # Calculate the count of good pairs for the current index `j`
            bad_pairs += j - freq_map.get(diff, 0)
            # Update the frequency map with the difference `nums[j] - j`
            freq_map[diff] = freq_map.get(diff, 0) + 1

        return bad_pairs

"""
# Intuition
The problem requires counting the number of bad pairs, which can be solved efficiently by counting the good pairs first and then subtracting them from the total pairs. A good pair satisfies the equation `j - i == nums[j] - nums[i]`, which can be rearranged to `nums[j] - j == nums[i] - i`. Using this property, we can leverage a frequency map to track the occurrences of `nums[k] - k` for all indices `k`.

# Approach
1. Use a frequency map to store the count of `nums[j] - j` values.
2. Iterate through the array and, for each index `j`, calculate the count of good pairs using the frequency map.
3. Subtract the count of good pairs from the total pairs to determine the number of bad pairs.

# Complexity
- Time complexity: O(n) since we iterate through the array once and dictionary operations (insertions and lookups) are O(1) on average.
- Space complexity: O(n) for the frequency map, which stores at most `n` unique keys.
"""
