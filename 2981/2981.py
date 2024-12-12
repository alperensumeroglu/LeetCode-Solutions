class Solution:
    def maximumLength(self, string: str) -> int:
        char_freq = defaultdict(lambda: defaultdict(int))
        curr_length = 0
        prev_char = -1
        
        for char in string:
            curr_length, prev_char = (curr_length + 1 if char == prev_char else 1), char
            char_freq[char][curr_length] += 1

        max_length = -1
        
        for char in char_freq.keys():
            count = 3
            for length in range(max(char_freq[char]), 0, -1):
                count -= char_freq[char][length]
                if count <= 0:
                    max_length = max(max_length, length)
                    break

        return max_length
