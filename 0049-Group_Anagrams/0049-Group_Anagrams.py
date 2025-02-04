
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to map character frequency tuples to a list of anagrams
        anagrams_map = defaultdict(list)
        
        for word in strs:
            # Initialize a frequency count for each letter (26 letters in the English alphabet)
            char_count = [0] * 26
            
            for char in word:
                # Increment the count at the index corresponding to the character
                char_count[ord(char) - ord('a')] += 1
            
            # Use the character count tuple as the key and append the word to the dictionary
            anagrams_map[tuple(char_count)].append(word)
        
        # Return the values of the dictionary, which are the grouped anagrams
        return list(anagrams_map.values())

'''
# Intuition
The problem requires grouping words that are anagrams of each other. An anagram contains the same characters in different orders, so the frequency of each character is the same for anagrams. This property helps us to group them.

# Approach
We use a dictionary to group words with the same character frequency. For each word, we calculate a character frequency count (a list of size 26 representing the counts of 'a' to 'z'). This list is converted into a tuple and used as a dictionary key to group anagrams.

# Complexity
- Time complexity: O(n * m), where n is the number of words and m is the average length of each word. We iterate through all characters of all words.
- Space complexity: O(n * m), to store the grouped anagrams and character frequency counts.
'''
