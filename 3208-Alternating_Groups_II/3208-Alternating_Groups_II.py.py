class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        """
        Intuition:
        - We need to count the number of contiguous alternating subarrays of length at least k.
        - An alternating group means that adjacent elements are different.

        Approach:
        - Maintain a counter `w` to track the length of the current alternating sequence.
        - Iterate through the colors array in a circular manner.
        - If the current color is different from the previous one, increment `w`.
        - Otherwise, reset `w` to 1.
        - If `w` reaches `k` or more, increment the result counter `ans`.
        
        Complexity:
        - Time Complexity: O(n) since we iterate through the array once.
        - Space Complexity: O(1) as we use only a few extra variables.
        """
        w = 1  # Tracks the length of the current alternating sequence
        ans = 0  # Counts valid alternating groups
        n = len(colors)
        
        for i in range(1, n + k - 2 + 1):  # Loop through circular array
            if colors[i % n] != colors[(i - 1 + n) % n]:  # Check if alternating
                w += 1  # Increase alternating sequence length
            else:
                w = 1  # Reset if pattern breaks
            
            if w >= k:
                ans += 1  # Count valid alternating groups
        
        return ans  # Return total count of valid alternating groups

# 🚀🔥 Keep coding and stay awesome!
