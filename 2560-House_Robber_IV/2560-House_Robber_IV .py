class Solution:
    def minCapability(self, nums, k):
        """
        Intuition:
        The robber must steal from at least `k` houses without robbing two adjacent houses.
        The goal is to minimize the maximum amount stolen from any house, ensuring an optimal selection.
        
        Instead of brute-forcing every possible combination (which is inefficient),  
        we use Binary Search on the answer:
        - We guess a capability (mid) and check if it allows robbing at least `k` houses.
        - If `mid` works, we try to lower it; otherwise, we increase it.

        Approach:
        1. Binary Search Setup:  
           - The robber's capability can range from `1` to `max(nums)`.
           - We initialize `left = 1` and `right = max(nums)`, and perform binary search.

        2. Greedy Feasibility Check:  
           - For each `mid` (potential capability), iterate through `nums`:  
             - Rob a house if its value is `≤ mid`.
             - Skip the next house to satisfy the non-adjacent constraint.
             - Track the total number of houses robbed (`ways`).
           - If `ways >= k`, then `mid` is a valid capability.

        3. Binary Search Update:  
           - If at least `k` houses can be robbed with `mid`, reduce `mid` (`right = mid`).
           - Otherwise, increase `mid` (`left = mid + 1`).

        4. Final Answer:  
           - The smallest possible `mid` that allows robbing at least `k` houses is returned.

        Complexity Analysis:
        - Time Complexity: O(n log(max(nums)))  
          Binary search runs in O(log(max(nums))) iterations, and each iteration does a linear O(n) check.
        - Space Complexity: O(1)  
          We only use a few integer variables (left, right, mid, ways, i), so the space complexity is constant.
        """

        # Define the binary search boundaries
        left, right = 1, max(nums)  # The minimum possible capability is 1, max is max(nums)

        while left < right:
            mid = (left + right) // 2  # Middle value as a candidate for maximum amount in a robbery
            ways = 0  # Count of non-adjacent houses that can be robbed
            i = 0  # Index pointer for house iteration

            # Iterate through the houses while ensuring non-adjacent selection
            while i < len(nums):
                if nums[i] <= mid:  # If the house can be robbed within the current capability
                    ways += 1  # Increase the number of chosen houses
                    i += 1  # Skip the next house to maintain non-adjacency
                i += 1  # Move to the next house
            
            # If at least k houses can be robbed, try to minimize the maximum capability
            if ways >= k:
                right = mid  # Narrow the search space towards a lower max capability
            else:
                left = mid + 1  # Increase the capability since we couldn't rob k houses
        
        return left  # The minimum maximum capability found
