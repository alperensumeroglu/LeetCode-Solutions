class Solution:
    def closestPrimes(self, left: int, right: int) -> list:
        """
        Finds the closest prime numbers in the given range [left, right].
        """
        
        def is_prime(n: int) -> bool:
            """ Checks if a number is prime. """
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        primes = []  # List to store prime numbers within the range
        
        for num in range(left, right + 1):
            if is_prime(num):
                primes.append(num)
            
            # If we find two primes with a gap of at most 2, return immediately
            if len(primes) >= 2 and primes[-1] - primes[-2] <= 2:
                return primes[-2:]
        
        # If there are at least two primes, return the closest pair found
        if len(primes) >= 2:
            return primes[-2:]
        
        # If no valid pair is found, return [-1, -1]
        return [-1, -1]

'''
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote
🔼 Please Upvote

💡If this helped, don’t forget to upvote! 🚀🔥

**Intuition**
The problem requires finding two closest prime numbers in a given range. The simplest way to do this is by iterating through the range, identifying prime numbers, and tracking the closest pair.

**Approach**
1. Use a helper function `is_prime()` to determine if a number is prime.
2. Iterate through the range `[left, right]` and collect prime numbers.
3. If a newly found prime forms a pair with a gap of 2 or less, return it immediately (as it's the optimal pair).
4. If no such immediate pair is found, return the closest pair.
5. If less than two primes exist, return `[-1, -1]`.

**Complexity**
- Time complexity: $$O(n \sqrt{m})$$ where $$n$$ is the range size and $$m$$ is the max number checked for primality.
- Space complexity: $$O(n)$$ for storing prime numbers.
'''
