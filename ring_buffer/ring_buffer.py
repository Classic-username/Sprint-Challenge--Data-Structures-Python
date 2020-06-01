from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.most_recently_used = None




    def append(self, item):
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.most_recently_used = self.storage.tail
            return

        if self.storage.length == self.capacity and self.storage.tail.next is None:
            self.storage.tail.next = self.storage.head

        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.most_recently_used = self.most_recently_used.next

        else:
            self.most_recently_used = self.most_recently_used.next
            self.most_recently_used.value = item
            
    def get(self):
        current = self.storage.head.next

        head_value = [self.storage.head.value]

        while current is not self.storage.head:
            if current is None:
                break

            head_value.append(current.value)
            current = current.next
        
        return head_value