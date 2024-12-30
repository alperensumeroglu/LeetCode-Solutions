class Solution:
    def numWays(self, strings: List[str], goal: str) -> int:
        def helper(target_idx, string_idx):
            if (target_idx, string_idx) in memoization:
                return memoization[(target_idx, string_idx)]

            if target_idx == goal_len:
                return 1

            if string_idx == string_len:
                return 0

            result = 0
            char = goal[target_idx]

            # Skip the current string_idx
            result += helper(target_idx, string_idx + 1)

            # Try to use the current string_idx
            if char in occurrences[string_idx]:
                result += helper(target_idx + 1, string_idx + 1) * occurrences[string_idx][char]

            memoization[(target_idx, string_idx)] = result
            return result

        modulo = 10**9 + 7
        goal_len = len(goal)
        string_len = len(strings[0])

        # Count occurrences of each character at each position
        occurrences = [defaultdict(int) for _ in range(string_len)]
        for i in range(string_len):
            for word in strings:
                character = word[i]
                occurrences[i][character] += 1

        memoization = {}
        return helper(0, 0) % modulo
