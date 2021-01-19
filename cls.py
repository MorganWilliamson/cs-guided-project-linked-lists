# Creating a Linked List in Python
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return f"Node({repr(self.value)})"

head = None

def insert_at_front(val):
    global head # Tell Python that head is a global variable, look for it out of scope

    # Make a new node
    new_node = Node(val)
    # Point new_node next at the head
    new_node.next = head
    # Point head to new_node
    head = new_node

def print_list():
    global head
    # Set cur to head
    cur = head

    # Loop while cur.next != None
    while cur is not None:
        # Print value at cur
        print(cur.value)
        # Set cur to cur.next
        cur = cur.next

insert_at_front(45)
insert_at_front(88)
