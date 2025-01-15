class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Counter to keep track of occurrences in both arrays
        frequency_map = collections.Counter()
        
        # Resultant array to store prefix common counts
        prefix_common_counts = []
        
        # Iterate over elements of A and B simultaneously
        for element_a, element_b in zip(A, B):
            # Increment count for elements from both arrays
            frequency_map[element_a] += 1
            frequency_map[element_b] += 1
            
            # Count elements appearing in both arrays (count == 2)
            common_count = sum(1 for key in frequency_map.keys() if frequency_map[key] == 2)
            
            # Append the common count to the result array
            prefix_common_counts.append(common_count)
        
        # Return the resulting prefix common array
        return prefix_common_counts
