class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize a dictionary to count occurrences of each character
        character_counts = {}
        for char in s:
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
        
        # Iterate through each character and its count
        for character, count in character_counts.items():
            remaining_count = count  # Initialize a variable to track reduced count
            
            # Reduce the count by 2 repeatedly as long as it's greater than 2
            while remaining_count > 2:
                remaining_count -= 2
            
            # Update the count in the dictionary
            character_counts[character] = remaining_count
        
        # Return the sum of all remaining counts
        return sum(character_counts.values())
