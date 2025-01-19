class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        n = len(derived)
        # Initialize the potential original array with a placeholder
        original = [-1] * n
        original[0] = 0  # Start with assuming the first element is 0

        # Iterate to reconstruct the original array
        for i in range(n):
            current_xor = derived[i]  # Current XOR value from derived array
            if i < n - 1:  # Reconstruct next element in original array
                if current_xor == 0:
                    original[i + 1] = original[i]
                else:
                    original[i + 1] = 1 - original[i]

            # Consistency check for the circular XOR condition at the end
            if i == n - 1:  # Last element XOR consistency check
                if current_xor == 0:
                    if original[n - 1] != original[0]:
                        return False
                else:
                    if original[n - 1] == original[0]:
                        return False

        return True