class Solution:
    def partitionLabels(self, s):
        """
        Partition the string into as many parts as possible so that each character appears in at most one part.
        Return the sizes of these partitions.
        
        Intuition:
        The goal is to split the string into segments where no character appears in more than one segment.
        To achieve this, we need to know the last occurrence of each character in the string. This helps us determine
        the farthest point we need to extend a partition to ensure all occurrences of a character are included.
        
        Approach:
        1. First, we create a dictionary to store the last occurrence index of each character in the string.
        2. We then iterate through the string, keeping track of the current partition's start and end indices.
        3. For each character, we update the end of the current partition to be the maximum of the current end
           and the last occurrence of the character.
        4. When we reach the end of the current partition (i.e., the current index equals the end), we record
           the partition's length and move the start to the next index.
           
        Complexity:
        - Time: O(n), where n is the length of the string. We traverse the string twice: once to build the last_occurrence dictionary and once to determine the partitions.
        - Space: O(1), since the last_occurrence dictionary stores at most 26 entries (for each lowercase English letter).
        """
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: index for index, char in enumerate(s)}
        
        partitions = []
        start, end = 0, 0  # Initialize the start and end of the current partition

        # Step 2: Iterate through the string to determine partitions
        for current_index, char in enumerate(s):
            # Update the end of the current partition to the farthest last occurrence of any character in the partition
            end = max(end, last_occurrence[char])
            
            # If the current index reaches the end of the partition, record the partition's length
            if current_index == end:
                partition_length = end - start + 1
                partitions.append(partition_length)
                start = current_index + 1  # Move the start to the next index for a new partition

        return partitions