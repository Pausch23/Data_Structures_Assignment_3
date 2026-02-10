# Name: Paul Schmidt
# OSU Email: schmipau@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Part 4
# Due Date: 2/9/2026
# Description: Stack class using singly linked list structure.
# Methods implemented to push, pop, and top values on the
# stack.


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
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
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Pushes value to top of the stack.

        :param value:   value to add to stack

        :return:        None
        """
        # Set new head node if list is empty
        if self.is_empty():
            self._head = SLNode(value, None)
        else:
            # Preserve head node and set new head node
            head_node = self._head
            self._head = SLNode(value, None)

            # Set new head node's next to preserved head node
            self._head.next = head_node


    def pop(self) -> object:
        """
        Removes top value from stack.

        :param :        None

        :return:        value from stack
        """
        # Raise exception if list is empty
        if self.is_empty():
            raise StackException

        # Preserve head node and set head to next
        curr_node = self._head
        self._head = curr_node.next

        # Return the preserved head node value
        return curr_node.value


    def top(self) -> object:
        """
        Returns top value of stack without changing stack.

        :param :        None

        :return:        top value from stack
        """
        # Raise exception if list is empty
        if self.is_empty():
            raise StackException

        # Return the preserved head node value
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# push example 1")
    # s = Stack()
    # print(s)
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s)

    # print("\n# pop example 1")
    # s = Stack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))


    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
