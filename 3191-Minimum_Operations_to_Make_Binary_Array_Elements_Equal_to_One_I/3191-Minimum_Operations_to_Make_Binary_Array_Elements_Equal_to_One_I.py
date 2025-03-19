class Solution:
    def minOperations(self, nums):
        """
        Intuition:
        We need to flip groups of three consecutive elements to turn all elements into 1s.
        If it's impossible, we return -1. 

        Approach:
        - Iterate through the list.
        - Whenever we find a `0`, we flip the current and the next two elements.
        - Count the number of flips needed.
        - After processing, check if all elements are `1`, otherwise return -1.

        Complexity:
        - Time Complexity: O(N), where N is the length of the array, as we traverse it once.
        - Space Complexity: O(1), since we modify the array in place without extra space.
        """
        n = len(nums)
        flip_count = 0  # Tracks number of operations performed

        for i in range(n - 2):  # Iterate up to n-2 to avoid out-of-bounds access
            if nums[i] == 0:  # If we find a zero, flip this and next two elements
                flip_count += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

        # After processing, check if all elements are now 1
        for num in nums:
            if num == 0:
                return -1
        return flip_count

# 🚀🔥 Keep coding and stay awesome!
