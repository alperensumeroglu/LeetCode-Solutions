class Solution:
    def largestDivisibleSubset(self, nums):
        # -----------------------------------------------------
        # 💡 Intuition:
        # We want to find the largest subset of numbers where for any two elements a and b, 
        # one divides the other (i.e., a % b == 0 or b % a == 0).
        # Sorting the array helps because any divisor of a number comes before it.
        # Then we can use Dynamic Programming to build up the solution.
        # -----------------------------------------------------

        # -----------------------------------------------------
        # 🧠 Approach:
        # 1. Sort the numbers in ascending order.
        # 2. Use a DP array where dp[i] stores the length of the largest subset ending at nums[i].
        # 3. For each number, check all previous numbers and update dp[i] if divisible.
        # 4. Track the maximum subset size and its ending index.
        # 5. Reconstruct the subset by walking backwards through the array.
        # 6. Reverse the result to return the subset in correct order.
        # -----------------------------------------------------

        # -----------------------------------------------------
        # ⏱️ Complexity:
        # Time Complexity: O(n^2), where n is the number of elements in the list.
        # - For each element, we may compare it with all previous elements.
        # Space Complexity: O(n)
        # - We use extra space for the dp array and the result list.
        # -----------------------------------------------------

        # Step 1: Sort the numbers so that divisors come before their multiples
        nums.sort()
        n = len(nums)

        # dp[i] will hold the size of the largest divisible subset ending with nums[i]
        dp = [1] * n

        # Variables to track the size and ending index of the maximum subset
        max_size = 1
        max_index = 0

        # Step 2: Fill the dp array using nested loops
        for i in range(1, n):
            for j in range(i):
                # If nums[i] is divisible by nums[j], it can be chained to the subset ending at nums[j]
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

            # Update the largest subset info if we found a longer one
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i

        # Step 3: Reconstruct the subset by walking backward from max_index
        result = []
        current_num = nums[max_index]
        current_size = max_size

        for i in range(max_index, -1, -1):
            # If the current number is divisible and matches the expected size
            if current_num % nums[i] == 0 and dp[i] == current_size:
                result.append(nums[i])
                current_num = nums[i]
                current_size -= 1

        # Since we collected elements in reverse order, reverse to return in ascending order
        result.reverse()
        return result
