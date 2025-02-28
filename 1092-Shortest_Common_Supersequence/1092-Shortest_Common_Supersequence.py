class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Get the lengths of both input strings
        rows, cols = len(str1) + 1, len(str2) + 1

        # Initialize the DP table with dimensions (rows x cols)
        dp = [[0] * cols for _ in range(rows)]

        # Fill the first row and first column with incremental values
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + 1
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + 1

        # Fill the DP table based on the shortest supersequence logic
        for r in range(1, rows):
            for c in range(1, cols):
                if str1[r - 1] == str2[c - 1]:  # If characters match
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:  # If characters differ, take the minimum cost option
                    dp[r][c] = min(dp[r - 1][c] + 1, dp[r][c - 1] + 1)

        # Backtrack to reconstruct the shortest common supersequence
        r, c = rows - 1, cols - 1
        result = []

        while r > 0 and c > 0:
            if str1[r - 1] == str2[c - 1]:  # If characters match, take one
                result.append(str1[r - 1])
                r -= 1
                c -= 1
            elif dp[r][c] == dp[r - 1][c] + 1:  # Take from str1
                result.append(str1[r - 1])
                r -= 1
            else:  # Take from str2
                result.append(str2[c - 1])
                c -= 1

        # Add remaining characters if any
        while r > 0:
            result.append(str1[r - 1])
            r -= 1
        while c > 0:
            result.append(str2[c - 1])
            c -= 1

        # Reverse to get correct order and return the result
        return ''.join(reversed(result))


'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

Intuition
When merging two strings to form the shortest common supersequence, we want to include all characters from both strings while maintaining the order of appearance. The idea is similar to finding the longest common subsequence (LCS) and then inserting missing characters to form the supersequence.

Approach
1. Use **Dynamic Programming (DP)** to compute a table where `dp[i][j]` stores the length of the shortest supersequence for substrings `str1[:i]` and `str2[:j]`.
2. Fill the DP table:
   - If characters at `str1[i-1]` and `str2[j-1]` are the same, inherit from `dp[i-1][j-1]` + 1.
   - Otherwise, take the minimum of inserting from `str1` or `str2` (`dp[i-1][j] + 1` or `dp[i][j-1] + 1`).
3. Backtrack through the table to reconstruct the shortest supersequence by:
   - Adding common characters when they match.
   - Adding characters from `str1` or `str2` based on which contributes to the minimum cost.
   - Finally, adding any leftover characters.
4. Reverse the reconstructed sequence to get the correct order.

Complexity
• Time complexity: **O(m * n)** where `m` and `n` are the lengths of `str1` and `str2`, as we compute a DP table of size `m x n` and backtrack through it.
• Space complexity: **O(m * n)** due to storing the DP table.
'''
