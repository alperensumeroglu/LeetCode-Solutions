class Solution:
    def maximumLength(self, string: str) -> int:
        char_freq = {}
        curr_length = 0
        prev_char = -1

        for char in string:
            if char == prev_char:
                curr_length += 1
            else:
                curr_length = 1
                prev_char = char
            
            if char not in char_freq:
                char_freq[char] = {}
            if curr_length not in char_freq[char]:
                char_freq[char][curr_length] = 0
            char_freq[char][curr_length] += 1

        max_length = -1

        for char in char_freq:
            count = 3
            lengths = sorted(char_freq[char].keys(), reverse=True)
            for length in lengths:
                count -= char_freq[char][length]
                if count <= 0:
                    max_length = max(max_length, length)
                    break

        return max_length
        