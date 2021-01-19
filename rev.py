# Reversing a Linked List
# "The solution everyone's always looking for is that the nodes don't change, but their POINTERS change."
## We change the direction of the pointers, put the head at the "end", and put None at the "beginning".
## Pointers, pointers, pointers!

# Beej Notes on reversing a linked list:
# "This one takes a head passed in, unlike the code we wrote in class, but could be easily modified."

def reverse(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have "fallen off" the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next 

        # Reverse the "next" pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node