class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MODULO = 1000000007  # We use modulo to avoid integer overflow for large numbers

        # -------------------- STEP 1: Find Prime Numbers --------------------
        # We need primes to store each number's prime factor exponents.
        # Example: 12 = 2^2 * 3^1 → we'll represent it as [2, 1, 0, ...] across all known primes

        primes = []
        number = 2
        while number <= maxValue:
            is_prime = True
            divisor = 2
            while divisor * divisor <= number:
                if number % divisor == 0:
                    is_prime = False
                    break
                divisor += 1
            if is_prime:
                primes.append(number)
            number += 1

        prime_count = len(primes)

        # -------------------- STEP 2: Precompute Factorials and Inverses --------------------
        # We'll use factorials to compute combinations (n choose k) efficiently.
        # comb(n + k - 1, k) is used to distribute k identical items across n slots (stars and bars method)

        MAX = n + 14  # Slight buffer for highest expected combination usage
        factorial = [1] * (MAX + 1)
        inv_factorial = [1] * (MAX + 1)

        # Precompute factorials
        i = 1
        while i <= MAX:
            factorial[i] = factorial[i - 1] * i % MODULO
            i += 1

        # Function to compute modular inverse using Fermat's Little Theorem
        def mod_inverse(x):
            result = 1
            power = MODULO - 2  # Since MODULO is prime
            while power > 0:
                if power % 2 == 1:
                    result = result * x % MODULO
                x = x * x % MODULO
                power //= 2
            return result

        # Precompute inverse factorials
        i = 0
        while i <= MAX:
            inv_factorial[i] = mod_inverse(factorial[i])
            i += 1

        # Compute combination C(a, b) = a! / (b! * (a-b)!)
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inv_factorial[b] % MODULO * inv_factorial[a - b] % MODULO

        # -------------------- STEP 3: Create Prime Factor Vectors for All Values --------------------
        # We'll compute prime factorization vector for each value up to maxValue
        # Each number is represented by the exponents of its prime factors in order

        factor_map = {1: [0] * prime_count}  # 1 has no prime factors

        val = 2
        while val <= maxValue:
            for i in range(prime_count):
                prime = primes[i]
                if val % prime == 0:
                    smaller = val // prime
                    if smaller in factor_map:
                        # Copy the vector of val // prime and add 1 to this prime's exponent
                        prev_vector = factor_map[smaller]
                        new_vector = []
                        j = 0
                        while j < prime_count:
                            new_vector.append(prev_vector[j])
                            j += 1
                        new_vector[i] += 1
                        factor_map[val] = new_vector
                        break  # only use smallest dividing prime to factorize step-by-step
            val += 1

        # -------------------- STEP 4: Count All Valid Ideal Arrays --------------------
        # For each number up to maxValue:
        # - Convert its prime factor vector into combination counts using stars and bars:
        #   C(exponent + n - 1, exponent)
        # - Multiply combinations for each prime factor
        # - Add to the result

        result = 0
        value = 1
        while value <= maxValue:
            vector = factor_map.get(value, [0] * prime_count)
            ways = 1  # Start with 1 because we're multiplying
            i = 0
            while i < prime_count:
                exponent = vector[i]
                if exponent > 0:
                    # Number of ways to distribute `exponent` factors across `n` positions
                    ways = ways * comb(exponent + n - 1, exponent) % MODULO
                i += 1
            result = (result + ways) % MODULO
            value += 1

        return result

# 🚀🔥 You just mastered optimized combinatorics with no libraries! Keep pushing boundaries and stay legendary.
