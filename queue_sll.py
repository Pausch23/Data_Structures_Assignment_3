# Name: Paul Schmidt
# OSU Email: schmipau@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Part 5
# Due Date: 2/9/2026
# Description: Queue class using the singly linked list
# structure for maintenance. Class has methods for
# enqueue, dequeue, and front.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        Adds value to end of the queue.

        :param value:   value to add

        :return:        None
        """
        # Set new head node if list is empty
        if self.is_empty():
            self._head = SLNode(value, None)
        else:
            # Preserve head node and set new head node
            head_node = self._head

            # Loop until the next node is None
            while head_node.next:
                head_node = head_node.next

            # Set the new node
            head_node.next = SLNode(value, None)


    def dequeue(self) -> object:
        """
        Removes value at the beginning of the queue.

        :param :   None

        :return:   value removed
        """
        # Raise exception if list queue is empty
        if self.is_empty():
            raise QueueException

        # Preserve head node
        head_node = self._head

        # Set head node to next node and return head node value
        self._head = head_node.next
        return head_node.value


    def front(self) -> object:
        """
        Returns front element of the queue without removing.

        :param :   None

        :return:   front value
        """
        # Raise exception if list is empty
        if self.is_empty():
            raise QueueException

        # Return the preserved head node value
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# enqueue example 1")
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)



    # print("\n# dequeue example 1")
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue())
    #     except Exception as e:
    #         print("No elements in queue", type(e))


    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
