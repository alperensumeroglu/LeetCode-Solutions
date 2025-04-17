class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        # ---------------------------------------------------------------------------- #
        # Intuition:
        # We are given an array and asked to count how many subarrays contain at least
        # 'k' good pairs. A good pair means nums[i] == nums[j] and i < j.
        # 
        # Brute force would check all subarrays and count pairs → O(n^2) or worse.
        # Instead, we use a sliding window and frequency map to count efficiently.
        # ---------------------------------------------------------------------------- #

        # ---------------------------------------------------------------------------- #
        # Approach:
        # - Use two pointers (left and right) to create a sliding window.
        # - Use a dictionary (frequency) to count the frequency of each number in the window.
        # - Every time we add a number to the window (moving right pointer), we calculate
        #   how many new good pairs this number forms with previous occurrences.
        # - When we reach a point where the current window has at least 'k' good pairs,
        #   we can count all subarrays that end at 'right' and start from left to right.
        # - Then we try to shrink the window from the left to find other valid subarrays.
        # ---------------------------------------------------------------------------- #

        frequency = {}  # Frequency map of numbers in the current window
        left = 0  # Left boundary of the sliding window
        current_pair_count = 0  # Number of good pairs in the current window
        total_good_subarrays = 0  # Final result

        # Right pointer iterates over the array
        for right in range(len(nums)):
            current_value = nums[right]

            # Count new good pairs formed by current_value
            if current_value in frequency:
                # If it appeared before, we can form new pairs
                current_pair_count += frequency[current_value]
                frequency[current_value] += 1
            else:
                # First time seeing this value in the current window
                frequency[current_value] = 1

            # While we have at least 'k' good pairs, move left pointer
            while current_pair_count >= k:
                # All subarrays from left to right are valid
                total_good_subarrays += len(nums) - right

                # Shrink the window from the left
                value_at_left = nums[left]
                frequency[value_at_left] -= 1

                # After removing one occurrence, lose that many pairs
                current_pair_count -= frequency[value_at_left]
                left += 1

        return total_good_subarrays

        # ---------------------------------------------------------------------------- #
        # Complexity:
        # Time Complexity: O(n)
        # - Each element is processed at most twice (once by right, once by left).
        #
        # Space Complexity: O(n)
        # - We store frequencies of numbers in the current window in a hash map.
        # ---------------------------------------------------------------------------- #

