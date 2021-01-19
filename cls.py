class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.fizz = 3490

    def __repr__(self):
        return f"Node({repr(self.value)})"

n = Node(45)
o = Node(88)

print(n.value)
print(o.value)
print(n.next)
print(n.fizz)