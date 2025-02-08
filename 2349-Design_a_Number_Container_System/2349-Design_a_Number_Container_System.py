
import heapq

class NumberContainers:
    def __init__(self):
        # Map indices to their numbers
        self.index_to_number = {}
        # Map numbers to their min-heaps of indices
        self.number_to_indices = {}

    def change(self, index: int, number: int) -> None:
        # Update the number at the given index
        self.index_to_number[index] = number
        
        # Create a min-heap for the number if it doesn't exist
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
        
        # Push the index to the min-heap of the given number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        # If the number doesn't exist, return -1
        if number not in self.number_to_indices:
            return -1

        # Get the heap of indices for the number
        possible_indices = self.number_to_indices[number]
        while possible_indices:
            # Check the smallest index in the heap
            smallest_index = possible_indices[0]
            
            # If the index is valid, return it
            if self.index_to_number[smallest_index] == number:
                return smallest_index
            
            # If the index is invalid, pop it from the heap
            heapq.heappop(possible_indices)
        
        # If no valid index is found, return -1
        return -1


"""
Intuition
The problem involves dynamically managing indices and numbers while ensuring efficient updates and queries. 
Using a combination of dictionaries and min-heaps, we can efficiently track and retrieve the smallest valid index for any given number.

Approach
1. Use a dictionary to map indices to the numbers assigned to them.
2. Use another dictionary to map numbers to min-heaps of indices.
3. When `change` is called:
   - Update the number at the given index.
   - Add the index to the min-heap for the new number.
4. When `find` is called:
   - Check the min-heap of indices for the given number.
   - Remove invalid indices until a valid one is found or the heap is empty.

Complexity
- Time complexity:
  - `change`: O(log n) for adding to the heap.
  - `find`: O(log n) for removing invalid indices from the heap.
- Space complexity: O(n), where n is the total number of indices stored.
"""
