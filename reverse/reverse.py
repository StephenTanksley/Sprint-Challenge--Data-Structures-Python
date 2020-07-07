class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        # # First case. Head value is none or is only value.
        if self.head is None or self.head.next_node is None:
            return self.head

        # # Second case: We have more than one item in the list.
        if node.next_node:
            # this is where the recursion is happening.
            self.reverse_list(node.next_node, node)

        # # Break condition - we reach the end and there's no next node.
        # Once self.head becomes our current node, we're all done.
        if node.next_node == None:
            self.head = node

        # # This is where the pointers are switched.
        # Prev is just a way of keeping track of where we came from.
        node.next_node = prev
