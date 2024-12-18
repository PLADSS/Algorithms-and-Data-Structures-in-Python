from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains
    Returns a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2

        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next
        mid_node.next = None

        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """

    # Create a new linked lisr that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        # If the head node of left is None, we're past the tail
        # Add the node from right to merged linked list
        if left_head is None:
            current.next = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next
        # If the head node of right is None, we're past the tail
        # Add the tail node from left to merged linked list
        elif right_head is None:
            current.next = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next
        else:
            # Not at either tail node
            # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            # If data on left is lesser than right set current to left node
            if left_data < right_data:
                current.next = left_head
                # Move left head to next node
                left_head = left_head.next
            # If data on left is greater than right set current to right node
            else:
                current.next = right_head
                # Move right head to next node
                right_head = right_head.next
        # Move current to next node
        current = current.next

    # Discard fake head and set first merged node as head
    head = merged.head.next
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(2)
l.add(8)
l.add(5)
l.add(300)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
