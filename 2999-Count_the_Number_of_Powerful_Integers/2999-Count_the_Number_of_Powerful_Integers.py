class Solution:
    def numberOfPowerfulInt(self, start, finish, limit, s):
        # ----------------------------------------------------------------------
        # Intuition:
        # We need to count how many integers in [start, finish] satisfy:
        # - The number ends with the string `s`.
        # - All digits before the suffix are ≤ `limit`.
        # Since brute-force is too slow for large ranges, we use Digit DP to count efficiently.
        # ----------------------------------------------------------------------

        def count(val):
            # ------------------------------------------------------------------
            # Approach:
            # 1. Convert `val` to string and split it into prefix and suffix.
            # 2. Build valid prefixes using only digits ≤ `limit`.
            # 3. Use a DP table: dp[i][tight] = number of valid ways to build digits
            #    starting from index i with `tight` constraint (whether still bound by `val`).
            # 4. At the end, check if the suffix of `val` is ≥ `s` for validity.
            # ------------------------------------------------------------------

            val_str = str(val)
            prefix_len = len(val_str) - len(s)

            # If val is shorter than suffix, it's invalid
            if prefix_len < 0:
                return 0

            # dp[i][tight] = number of valid prefixes starting at index i
            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            # Base case: reached suffix, count depends on whether suffix is valid
            dp[prefix_len][0] = 1  # No constraint case
            dp[prefix_len][1] = int(val_str[prefix_len:] >= s)

            # Fill DP table backwards
            for i in range(prefix_len - 1, -1, -1):
                current_digit = int(val_str[i])

                # Case: tight = 0 → full freedom
                dp[i][0] = (limit + 1) * dp[i + 1][0]

                # Case: tight = 1 → constrained by val_str[i]
                if current_digit <= limit:
                    dp[i][1] = current_digit * dp[i + 1][0] + dp[i + 1][1]
                else:
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            # Start from the first digit with tight constraint
            return dp[0][1]

        # ------------------------------------------------------------------
        # Final Result:
        # Count how many valid numbers ≤ finish, then subtract those < start.
        # This gives us count in [start, finish].
        # ------------------------------------------------------------------
        return count(finish) - count(start - 1)

        # ------------------------------------------------------------------
        # Complexity:
        # Time: O(D * 2), where D is number of digits (up to 10)
        # Space: O(D * 2) for DP table
        # Efficient even for very large ranges (up to 10^9)
        # ------------------------------------------------------------------

# 🚀🔥 Keep coding and stay awesome! Your logic skills are leveling up!
