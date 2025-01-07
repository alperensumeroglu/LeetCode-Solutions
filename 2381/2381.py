class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        # Length of the input string
        n = len(s)

        # Initialize a delta array to track shifts
        shift_changes = [0] * (n + 1)

        # Process each shift operation
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                shift_changes[start] += 1
                shift_changes[end + 1] -= 1
            else:  # Backward shift
                shift_changes[start] -= 1
                shift_changes[end + 1] += 1

        # Accumulate the net shift at each position
        for i in range(1, n):
            shift_changes[i] += shift_changes[i - 1]

        # Build the resulting string
        result = []
        base_ord = ord('a')
        for i, char in enumerate(s):
            # Calculate new character after applying shifts
            new_char = chr((ord(char) - base_ord + shift_changes[i]) % 26 + base_ord)
            result.append(new_char)

        # Return the final shifted string
        return ''.join(result)
