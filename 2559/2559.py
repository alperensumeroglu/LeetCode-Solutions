class Solution:
    def vowelStrings(self, words, queries):
        # Definition of vowels
        vowels = "aeiou"
        
        # Helper function: checks if a word starts and ends with a vowel
        def is_vowel_string(word):
            if word[0] in vowels and word[-1] in vowels:
                return 1  # The word starts and ends with a vowel
            return 0  # The word does not satisfy the condition
        
        # List to check if each word is a vowel string (1 for yes, 0 for no)
        vowel_flags = [is_vowel_string(word) for word in words]
        
        # Create a prefix sum array to store cumulative sums
        prefix_sum = [0] * (len(vowel_flags) + 1)
        for i in range(len(vowel_flags)):
            prefix_sum[i + 1] = prefix_sum[i] + vowel_flags[i]
        
        # Calculate the results for each query
        results = []
        for left, right in queries:
            # Calculate the count of vowel strings in the range [left, right]
            count = prefix_sum[right + 1] - prefix_sum[left]
            results.append(count)
        
        return results
