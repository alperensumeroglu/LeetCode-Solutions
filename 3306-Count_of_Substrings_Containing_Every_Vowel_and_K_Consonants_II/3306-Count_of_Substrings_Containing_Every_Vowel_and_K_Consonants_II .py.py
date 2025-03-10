class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        # Set of vowels for quick lookup
        is_vowel = {char: True for char in "aeiou"}  
        
        # Dictionary to store vowel frequencies
        freq = {}  
        
        # Variables to track results and window properties
        response = 0
        current_k = 0  # Count of consonants in the window
        vowel_count = 0  # Number of distinct vowels in the window
        extra_left = 0  # Tracks how many extra vowels can be removed
        left = 0  # Left pointer of the sliding window

        # Iterate over the string using a sliding window
        for right in range(len(word)):
            right_char = word[right]

            # If the character is a vowel, update its frequency
            if right_char in is_vowel:
                freq[right_char] = freq.get(right_char, 0) + 1
                if freq[right_char] == 1:  # New distinct vowel found
                    vowel_count += 1
            else:
                current_k += 1  # Increase consonant count

            # Shrink the window if consonant count exceeds k
            while current_k > k:
                left_char = word[left]
                if left_char in is_vowel:
                    freq[left_char] -= 1
                    if freq[left_char] == 0:
                        vowel_count -= 1  # Remove from distinct vowel count
                else:
                    current_k -= 1
                left += 1
                extra_left = 0  # Reset extra vowel count

            # Adjust left pointer to remove extra vowels while maintaining k consonants
            while vowel_count == 5 and current_k == k and left < right and word[left] in is_vowel and freq[word[left]] > 1:
                extra_left += 1
                freq[word[left]] -= 1
                left += 1

            # If we have exactly k consonants and all 5 vowels, count substrings
            if current_k == k and vowel_count == 5:
                response += (1 + extra_left)

        return response

    """
    Intuition:
    - The goal is to find substrings containing exactly k consonants and all 5 vowels at least once.
    - We use a sliding window approach to efficiently track substrings that satisfy these constraints.
    
    Approach:
    - Maintain a frequency dictionary for vowels.
    - Use a sliding window with two pointers (left, right) to expand and shrink the window.
    - Ensure exactly k consonants are present in the window.
    - Count the number of substrings when all 5 vowels appear.
    
    Complexity:
    - Time Complexity: O(N), since each character is processed at most twice.
    - Space Complexity: O(1), since we use a fixed-size dictionary for vowels.
    
    🚀🔥 Keep coding and stay awesome!
    """
