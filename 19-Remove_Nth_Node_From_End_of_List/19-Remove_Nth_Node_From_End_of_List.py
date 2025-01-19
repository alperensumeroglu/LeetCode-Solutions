class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., removing the head node)
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, both starting at the dummy node
        first_pointer = dummy
        second_pointer = dummy

        # Move the first pointer n+1 steps ahead to maintain a gap of n nodes
        for _ in range(n + 1):
            first_pointer = first_pointer.next

        # Move both pointers one step at a time until the first pointer reaches the end
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        # Remove the nth node from the end by skipping it in the linked list
        second_pointer.next = second_pointer.next.next

        # Return the updated list starting from the original head
        return dummy.next