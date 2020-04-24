from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        if self.capacity == self.storage.length:
                if self.current is not None:
                    self.current = self.storage.head
                else:
                    self.current = None
          

                if self.current.value == self.storage.head.value:
                    self.storage.remove_from_head()
                    self.storage.add_to_head(item)
                    self.current = self.current.next
                else:
                    self.current.insert_after(item)
                    if self.current.next.next:
                        new_current = self.current.next.next
                    else:
                        new_current = self.storage.head
                    self.storage.delete(self.current)
                    self.storage.length += 1
                    self.current = new_current
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head

        while node:
            list_buffer_contents.append(node.value)
            node = node.next           

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
