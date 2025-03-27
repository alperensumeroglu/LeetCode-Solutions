class Solution:
    def minimumIndex(self, nums):
        """
        Intuition:
        The array has exactly one dominant element — an element that appears more than half the time.
        We want to split the array into two parts at some index `i` so that:
            - Both parts have the same dominant element.
            - The dominant element remains dominant in both parts.

        The key insight is:
        If we know how many times the dominant element appears in both the left and right parts
        for each possible split index, we can check whether it remains dominant in both subarrays.

        Approach:
        1. First, find the dominant element in the entire array by counting frequencies.
        2. Build two helper arrays:
            - `prefix[i]`: the number of times the dominant element appears from index 0 to i.
            - `suffix[i]`: the number of times the dominant element appears from index i to end.
        3. For each index `i` (from 0 to n-2), try splitting the array into two parts:
            - Left: nums[0 to i] → length = i + 1
            - Right: nums[i+1 to n-1] → length = n - (i + 1)
        4. Check if the dominant element appears more than half in both parts.
        5. The first index that satisfies this condition is the answer.

        Complexity:
        Time Complexity:
            - O(n) to count frequencies and find the dominant element.
            - O(n) to build prefix and suffix arrays.
            - O(n) to scan and check valid splits.
            => Total: O(n)
        
        Space Complexity:
            - O(n) for prefix and suffix arrays.
            => Total: O(n)
        """

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        # Step 1: Count frequency of each element
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Find the dominant element
        dominant = -1
        max_count = -1
        for num in frequency:
            if frequency[num] > max_count:
                max_count = frequency[num]
                dominant = num

        # Step 2: Build prefix array (count of dominant element up to index i)
        count = 0
        for i in range(n):
            if nums[i] == dominant:
                count += 1
            prefix[i] = count

        # Step 3: Build suffix array (count of dominant element from index i to end)
        count = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == dominant:
                count += 1
            suffix[i] = count

        # Step 4: Try each split point
        for i in range(n - 1):
            left_len = i + 1
            right_len = n - left_len
            left_count = prefix[i]
            right_count = suffix[i + 1]

            # Check if dominant is dominant in both halves
            if left_count * 2 > left_len and right_count * 2 > right_len:
                return i  # Found the minimum valid split index

        return -1  # No valid split exists
