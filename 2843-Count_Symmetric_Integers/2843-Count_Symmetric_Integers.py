class Solution:
    def countSymmetricIntegers(self, low, high):
        """
        Intuition:
        We are asked to count "symmetric integers" in a range. A number is symmetric if:
        - It has an even number of digits.
        - The sum of the first half digits equals the sum of the second half digits.
        This is a classic case of digit manipulation.

        Approach:
        1. Iterate through every number from `low` to `high` (inclusive).
        2. Convert each number to a string to easily access its digits.
        3. Skip the number if it has an odd number of digits (not eligible for symmetry).
        4. Split the string in half.
        5. Compute the sum of digits in both halves.
        6. If the sums are equal, increment the counter.
        7. Finally, return the total count of symmetric integers found.

        Complexity:
        - Time Complexity: O(N * D), where N is the number of integers in the range,
          and D is the average number of digits (since we compute digit sums).
        - Space Complexity: O(1), as we use a constant amount of extra space (excluding input size).
        """

        count = 0  # Counter to store the number of symmetric integers found

        for number in range(low, high + 1):
            string_number = str(number)  # Convert number to string to access digits
            num_digits = len(string_number)

            if num_digits % 2 != 0:
                continue  # Skip if number of digits is odd

            half = num_digits // 2  # Midpoint to divide the number
            # Sum the digits in the first half
            left_sum = sum(int(string_number[i]) for i in range(half))
            # Sum the digits in the second half
            right_sum = sum(int(string_number[i]) for i in range(half, num_digits))

            if left_sum == right_sum:
                count += 1  # Symmetric integer found

        return count
