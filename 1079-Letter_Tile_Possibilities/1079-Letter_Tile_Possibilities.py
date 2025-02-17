class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Create a frequency dictionary manually without using Counter
        char_count = {}
        for char in tiles:
            char_count[char] = char_count.get(char, 0) + 1

        def backtrack() -> int:
            total_sequences = 0  # Store the count of unique sequences
            
            for char in char_count:
                if char_count[char] > 0:
                    # Use the current character
                    char_count[char] -= 1
                    total_sequences += 1
                    
                    # Recurse to explore further sequences
                    total_sequences += backtrack()
                    
                    # Backtrack: Restore the character count
                    char_count[char] += 1
            
            return total_sequences

        return backtrack()


'''# Intuition
The problem requires us to generate all possible non-empty sequences from the given set of tiles. Since tiles can have duplicate letters, we need to account for repeated sequences.

# Approach
We use **backtracking** to explore all possible sequences while keeping track of character frequencies to avoid duplicate sequences. The approach follows these steps:
1. Create a frequency dictionary manually to store occurrences of each character.
2. Recursively build sequences by choosing a character, decrementing its count, and exploring further.
3. Backtrack by restoring the character count after recursive calls to ensure all combinations are explored.
4. The base case of recursion is when no characters are available for selection.

# Complexity
- **Time complexity:** \( O(k!) \) where \( k \) is the number of distinct letters in `tiles`. Each character can be used in different positions, leading to factorial growth.
- **Space complexity:** \( O(k) \) due to the recursion depth in the backtracking function.

'''