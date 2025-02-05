class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Initialize two pointers to traverse both linked lists
        pointerA, pointerB = headA, headB

        # Traverse both lists until the pointers meet or reach the end
        while pointerA != pointerB:
            # Move the pointer to the next node, or switch to the other list's head if null
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # Return the intersection node (or null if no intersection exists)
        return pointerA

"""
Intuition
To find the intersection of two linked lists, we can leverage the idea of equalizing their lengths by traversing both lists fully. If there's an intersection, the pointers will meet at the intersecting node; otherwise, they will both reach the end (null).

Approach
1. Initialize two pointers, one for each linked list.
2. Traverse through the lists:
   - If a pointer reaches the end of a list, redirect it to the head of the other list.
   - This ensures that both pointers traverse an equal number of nodes.
3. The loop exits when the two pointers meet, which is the intersection node, or both become null (no intersection).

Complexity
- Time complexity: O(n + m), where n and m are the lengths of the two linked lists.
  Both pointers traverse the combined length of the lists once.
- Space complexity: O(1), as no extra space is used.
"""
