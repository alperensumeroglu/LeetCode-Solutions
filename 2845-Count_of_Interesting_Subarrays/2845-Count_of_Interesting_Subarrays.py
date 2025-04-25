from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        """
        Counts the number of 'interesting' subarrays in the given list.
        A subarray is interesting if the number of elements nums[i] such that nums[i] % modulo == k
        is congruent to k modulo `modulo`.

        Intuition:
        -----------
        We want to count the subarrays where the count of elements satisfying nums[i] % modulo == k
        is such that the count % modulo == k. This hints towards prefix sums and modular arithmetic.
        
        Approach:
        ---------
        1. Use a prefix count (`pref`) to store how many times nums[i] % modulo == k has occurred so far.
        2. For each element in `nums`, check if it contributes to the count (i.e., nums[i] % modulo == k).
        3. The number of valid previous prefix counts that can form a valid subarray with the current index
           can be found by the formula: (current_pref - k) % modulo.
        4. Store and update counts of all `pref % modulo` values seen so far using a dictionary.
        5. Accumulate all valid subarray counts into `ans`.

        Complexity:
        -----------
        - Time Complexity: O(n), where n is the length of `nums`, because we loop through the array only once.
        - Space Complexity: O(modulo), for storing prefix frequencies (bounded by the value of `modulo`).

        Let's code this! 🧠
        """

        total_interesting_subarrays = 0  # Final result
        prefix_count = 0  # Tracks how many qualifying elements seen so far
        prefix_mod_count = defaultdict(int)  # Maps prefix % modulo to its frequency
        prefix_mod_count[0] = 1  # Base case: zero prefix before starting

        for num in nums:
            # Check if the current element satisfies nums[i] % modulo == k
            if num % modulo == k:
                prefix_count += 1

            # Compute the needed prefix mod value to form a valid subarray
            target_mod = (prefix_count - k) % modulo

            # Add to result the number of previous prefixes that match this mod
            total_interesting_subarrays += prefix_mod_count[target_mod]

            # Update the frequency of the current prefix mod
            prefix_mod_count[prefix_count % modulo] += 1

        return total_interesting_subarrays
