class Solution:
    def maximumCandies(self, candies, k):
        # Intuition:
        # We want to find the maximum number of candies each child can receive.
        # The solution must allow us to divide the candy piles optimally,
        # making sure we distribute candies evenly to exactly k children.

        # Approach:
        # We'll use Binary Search because the answer range is clearly defined (between 1 and max(candies)).
        # In each iteration, we'll check if it's possible to distribute candies with the mid-value number of candies.
        # If possible, we'll try a higher number; if not, we'll try a lower number.

        # Complexity:
        # Time: O(n * log(max(candies))) due to binary search and summing each time
        # Space: O(1) constant extra space

        # Check if total candies are fewer than children, meaning impossible distribution
        if sum(candies) < k:
            return 0

        # Initialize binary search bounds
        min_candies, max_candies = 1, max(candies)
        optimal_candies = 0  # stores the maximum candies each child can get

        while min_candies <= max_candies:
            mid_candies = (min_candies + max_candies) // 2

            # Count how many children can receive candies if each gets mid_candies
            children_count = sum(candy_pile // mid_candies for candy_pile in candies)

            if children_count >= k:
                # If it's possible, this is a potential solution; try to find a better (higher) one
                optimal_candies = mid_candies
                min_candies = mid_candies + 1
            else:
                max_candies = mid_candies - 1

        return optimal_candies

# 🚀🔥 Keep coding and stay awesome!