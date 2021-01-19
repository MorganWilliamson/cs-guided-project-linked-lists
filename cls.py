# Creating a Linked List in Python
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return f"Node({repr(self.value)})"

# Setting initial value (head), and a separate value (o)
head = Node(45)
o = Node(88)

# Making another reference point to 88, head now moves to o. 
head.next = o 

print(head.value)
print(o.value)
print(head.next)