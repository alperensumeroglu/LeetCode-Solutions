class Solution:
    def canPartition(self, nums):
        """
        Determines if the input list can be partitioned into two subsets with equal sum.

        Intuition:
        ----------
        The goal is to determine if we can split the input array into two subsets such that the sum of elements
        in both subsets is equal. If we can find **any subset** whose sum equals half of the total sum of the array,
        the other subset will automatically have the same sum (since total = sum1 + sum2, and we want sum1 == sum2).

        Approach:
        ---------
        1. Compute the total sum of all elements.
        2. If the total is odd, we cannot divide it into two equal parts → return False.
        3. Our new target becomes total // 2.
        4. Use a set to store all possible subset sums we can form.
        5. Iterate through each number:
           - For every possible sum already in the set, add the current number and store the new sum.
           - If at any point we reach the target sum, return True immediately.
        6. If we finish looping and still haven't found the target, return False.

        Complexity:
        -----------
        Time Complexity: O(n * target), where n is the number of elements and target = total // 2.
        Space Complexity: O(target), since the set stores all reachable subset sums up to the target.
        """

        # Step 1: Calculate the total sum of the array
        total = sum(nums)

        # Step 2: If the total sum is odd, it's impossible to divide it into two equal integers
        if total % 2 != 0:
            return False

        # Step 3: Our goal is to find if there's a subset that sums to exactly half the total
        target = total // 2

        # Step 4: Initialize a set to keep track of possible subset sums
        # Start with 0 because the sum of an empty subset is 0
        possible_sums = set([0])

        # Step 5: Iterate through each number in the array
        for num in nums:
            # We store new sums temporarily to avoid modifying the set while iterating
            current_sums = list(possible_sums)

            # Check all previously reachable sums and add the current number to them
            for current_sum in current_sums:
                new_sum = current_sum + num

                # If this new sum equals the target, we can partition the array
                if new_sum == target:
                    return True

                # Only add new sums that are less than the target to keep set size optimal
                if new_sum < target:
                    possible_sums.add(new_sum)

        # Step 6: If we exit the loop and haven't found the target, return False
        return False
