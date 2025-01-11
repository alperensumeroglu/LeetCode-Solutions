class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        # Function to check if one word is both a prefix and a suffix of another
        def isPrefixAndSuffix(prefix_candidate: str, target: str) -> bool:
            is_prefix = False
            is_suffix = False
            
            # A prefix cannot be longer than the target
            if len(prefix_candidate) > len(target):
                return False

            # Check if prefix_candidate is a prefix of target
            i = 0
            j = 0
            while i < len(prefix_candidate):
                if prefix_candidate[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    break
            if i == len(prefix_candidate):
                is_prefix = True

            # Check if prefix_candidate is a suffix of target
            i = len(prefix_candidate) - 1
            j = len(target) - 1
            while i >= 0:
                if prefix_candidate[i] == target[j]:
                    i -= 1
                    j -= 1
                else:
                    break
            if i < 0:
                is_suffix = True

            # Return True if both conditions are satisfied
            return is_prefix and is_suffix

        # Initialize the count of valid (i, j) pairs
        total_count = 0

        # Iterate through all possible (i, j) pairs in the words list
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    total_count += 1

        # Return the total count of valid pairs
        return total_count
