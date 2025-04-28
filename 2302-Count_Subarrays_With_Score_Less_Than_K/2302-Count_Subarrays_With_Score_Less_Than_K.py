from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        Intuition:
        - We are given an array of integers and an integer k.
        - We need to find the number of subarrays where (sum of elements) * (length of subarray) < k.
        - A brute-force solution checks every subarray, but it is too slow for large inputs.
        - We need an optimized approach using sliding window technique to speed it up.
        
        Approach:
        1. Initialize two pointers: 'start' (left) and 'end' (right) for the sliding window.
        2. Keep a running total 'current_sum' of elements between start and end.
        3. Expand the window by moving 'end' to the right, adding nums[end] to current_sum.
        4. If (current_sum) * (window length) >= k, shrink the window from the left (move 'start' right and update current_sum).
        5. After ensuring (current_sum) * (window length) < k, 
           the number of valid subarrays ending at 'end' is (end - start + 1).
        6. Accumulate this count into the total 'count'.
        
        Complexity:
        - Time Complexity: O(n), because each element is visited at most twice (once by 'end' and once by 'start').
        - Space Complexity: O(1), using only a few variables.
        """

        count = 0        # Total count of valid subarrays
        current_sum = 0   # Running sum of the current window
        start = 0         # Left boundary of the window

        # Iterate through the array with 'end' as the right boundary
        for end in range(len(nums)):
            current_sum += nums[end]  # Add current element to the window

            # While the condition is violated, shrink the window from the left
            while current_sum * (end - start + 1) >= k:
                current_sum -= nums[start]  # Remove nums[start] from current_sum
                start += 1                 # Move start to the right

            # All subarrays ending at 'end' and starting from [start to end] are valid
            count += end - start + 1

        return count

# 🚀🔥 Keep coding and stay awesome! Mastery is built one problem at a time!
