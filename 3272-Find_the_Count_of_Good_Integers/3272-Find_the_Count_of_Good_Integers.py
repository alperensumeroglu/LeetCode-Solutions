class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # -------------------- Intuition --------------------
        # We aim to count all n-digit palindromic numbers that are divisible by k.
        # For each such number, we track its digit frequency pattern.
        # We only count distinct digit frequency patterns.
        # For each unique pattern, we calculate how many valid n-digit numbers
        # (with those exact digit counts) exist, considering the no-leading-zero rule.

        # -------------------- Approach --------------------
        # 1. Generate all palindromic numbers by creating and mirroring half-strings.
        # 2. Check divisibility by k.
        # 3. Count digit frequencies of valid palindromes.
        # 4. Encode frequency vectors uniquely using base-11 encoding.
        # 5. For each unique encoded frequency, calculate the number of valid permutations.
        
        # Helper function to compute combination (n choose r) without importing math
        def combination(n, r):
            if r > n or r < 0:
                return 0  # Invalid case
            result = 1
            for i in range(1, r + 1):
                result = result * (n - i + 1) // i  # Iteratively build combination
            return result

        # Determine how many digits to generate for half-palindrome
        # For example, if n = 5, we generate half as 3 digits → [abc] + [ba]
        half_length = (n + 1) // 2

        # The smallest number with half_length digits
        lower_limit = 10 ** (half_length - 1)
        # The smallest number with (half_length + 1) digits (exclusive upper limit)
        upper_limit = 10 ** half_length

        # Set to store encoded digit frequency patterns (base-11 encoded)
        encoded_frequencies = set()

        # Iterate over all possible half-palindromes
        for half in range(lower_limit, upper_limit):
            half_str = str(half)

            # Generate full palindromic number by mirroring
            if n % 2 == 0:
                # Even length: e.g., 12 -> 1221
                full_str = half_str + half_str[::-1]
            else:
                # Odd length: e.g., 123 -> 12321 (middle digit not repeated)
                full_str = half_str + half_str[:-1][::-1]

            # Convert the string back to an integer
            palindrome_number = int(full_str)

            # Only consider numbers divisible by k
            if palindrome_number % k == 0:
                # Count digit frequencies in the palindrome
                digit_count = [0] * 10  # 0–9 digit frequencies
                for char in full_str:
                    digit_count[int(char)] += 1

                # Encode frequency vector to a unique number using base-11
                encoded = 0
                for count in digit_count:
                    encoded = encoded * 11 + count  # Each count fits in base-11
                encoded_frequencies.add(encoded)  # Only keep unique patterns

        # Total number of valid permutations from all unique digit frequency patterns
        total_valid_permutations = 0

        # Decode each encoded frequency and compute permutations
        for code in encoded_frequencies:
            digit_count = [0] * 10
            temp = code

            # Decode base-11 encoded digit counts back into frequency list
            for i in range(9, -1, -1):
                digit_count[i] = temp % 11
                temp //= 11

            remaining_digits = n  # Number of places to fill
            permutations = 1  # Start with multiplicative identity

            # For each digit, compute how many ways to place it
            for digit in range(10):
                if digit_count[digit] > remaining_digits:
                    # If we want to use more digits than we have, invalid case
                    permutations = 0
                    break

                if digit == 0:
                    # Leading zeros are not allowed → we cannot place 0 at first position
                    # So reduce one place to avoid leading 0
                    permutations *= combination(remaining_digits - 1, digit_count[digit])
                else:
                    # Valid placements for this digit
                    permutations *= combination(remaining_digits, digit_count[digit])

                # Decrease available digits for the next iterations
                remaining_digits -= digit_count[digit]

            # Accumulate total valid permutations
            total_valid_permutations += permutations

        # -------------------- Complexity --------------------
        # Time Complexity:
        # - Palindrome generation: O(10^(n/2)) for generating half-strings.
        # - For each valid palindrome: O(n) for digit counting and encoding.
        # - For each unique encoded frequency: O(n) to decode and calculate permutations.
        # Space Complexity:
        # - O(U) where U is the number of unique encoded digit frequency patterns.

        return total_valid_permutations
