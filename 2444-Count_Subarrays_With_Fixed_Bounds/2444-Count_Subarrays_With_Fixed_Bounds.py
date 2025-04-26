class Solution:
    """
    Intuition:
    We want to count the number of contiguous subarrays where the minimum element is at least `minK`
    and the maximum element is at most `maxK`. By tracking the most recent positions of values 
    outside the [minK, maxK] range, as well as the latest occurrences of minK and maxK themselves,
    we can efficiently compute the contribution of each new element in a single pass.

    Approach:
    1. Initialize:
       - total_count: accumulator for valid subarrays.
       - last_invalid_index: the index of the most recent element < minK or > maxK.
       - last_min_index: the index of the most recent element equal to minK.
       - last_max_index: the index of the most recent element equal to maxK.
    2. Iterate through nums with index i:
       a. If nums[i] is out of the [minK, maxK] bounds:
          update last_invalid_index = i
       b. If nums[i] == minK:
          update last_min_index = i
       c. If nums[i] == maxK:
          update last_max_index = i
       d. The number of new valid subarrays ending at i is:
          max(0, min(last_min_index, last_max_index) - last_invalid_index)
       e. Add that to total_count.
    3. Return total_count.

    Complexity:
    - Time Complexity: O(n), we make a single pass through the list.
    - Space Complexity: O(1), only a handful of integer variables are maintained.
    """

    def countSubarrays(self, nums, minK, maxK):
        # Initialize counters and trackers
        total_count = 0
        last_invalid_index = -1
        last_min_index = -1
        last_max_index = -1

        # Traverse the array exactly once
        for i, value in enumerate(nums):
            # If value is out of the permitted range, mark this as a break point
            if value < minK or value > maxK:
                last_invalid_index = i

            # Update the most recent positions of minK and maxK
            if value == minK:
                last_min_index = i
            if value == maxK:
                last_max_index = i

            # Compute number of valid subarrays ending here
            valid_subarrays_ending_here = max(0, min(last_min_index, last_max_index) - last_invalid_index)
            total_count += valid_subarrays_ending_here

        return total_count


# 🚀🔥 Keep coding and stay awesome!
