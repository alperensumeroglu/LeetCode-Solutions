class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Determine the total number of boxes
        n = len(boxes)
        # Create a list to store the results
        operations = []
        
        # Calculate the number of operations for each box
        for current_box in range(n):
            # Total moves needed to bring all balls to the current box
            total_moves = 0
            
            # Check the boxes on the left
            for left_box in range(current_box - 1, -1, -1):
                # If the box contains a ball (1), add the move count
                if boxes[left_box] == "1":
                    total_moves += current_box - left_box
            
            # Check the boxes on the right
            for right_box in range(current_box + 1, n):
                # If the box contains a ball (1), add the move count
                if boxes[right_box] == "1":
                    total_moves += right_box - current_box
            
            # Add the total moves required for this box to the list
            operations.append(total_moves)
        
        # Return the results
        return operations
