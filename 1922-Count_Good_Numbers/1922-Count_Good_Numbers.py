class Solution:
    def countGoodNumbers(self, n: int):
        # Modulo value to prevent overflow in large computations
        mod = 10**9 + 7

        # -------------------------------
        # 🚀 Approach:
        # Step 1: Calculate number of digits at even indices (0, 2, 4, ...)
        #         These positions accept 5 possible digits.
        even_index_count = (n + 1) // 2

        # Step 2: Calculate number of digits at odd indices (1, 3, 5, ...)
        #         These positions accept 4 possible digits.
        odd_index_count = n // 2

        # Step 3: Use modular exponentiation to calculate:
        #         - pow(5, even_index_count, mod): number of ways for even indices
        #         - pow(4, odd_index_count, mod): number of ways for odd indices
        #         Multiply them under modulo.
        # -------------------------------

        total_combinations = (pow(5, even_index_count, mod) * pow(4, odd_index_count, mod)) % mod
  
        return total_combinations
