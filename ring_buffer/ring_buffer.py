"""
A ring buffer is going to use essentially a queue data structure. 
But instead of a queue that just keeps on going, this queue is 
going to have a fixed number of items that it keeps in storage.

Once we hit a certain length, the item at the top of the queue 
is going to be popped off to make room for the next item.
"""


class RingBuffer:
    def __init__(self, capacity):
        # We need a way to keep track of capacity.
        self.capacity = capacity
        self.data = []
        self.data_index = None

    def append(self, item):
        # This method will add an element to the buffer.

        # If we're already at capacity, it will dynamically update the position we're overwriting.
        if len(self.data) == self.capacity:

            # We're making a change to the array data_index and then overwriting that value.
            self.data[self.data_index] = item

            # We set the data index equal to the remainder of our current index plus 1 divided by the buffer's capacity.
            self.data_index = (self.data_index + 1) % self.capacity

            # This is the base case. We haven't hit capacity yet. Just append the item and update the index.
        else:
            self.data.append(item)
            # The if statement won't actually be fully triggered until we hit our capacity.
            if len(self.data) == self.capacity:
                print("Capacity reached! Overwriting data now...")
                self.data_index = 0

    def get(self):
        print(self.data)
        return self.data


rb = RingBuffer(3)

rb.append(3)
rb.append(65)
rb.append(6)
rb.append(7)
rb.append(20)

rb.get()
