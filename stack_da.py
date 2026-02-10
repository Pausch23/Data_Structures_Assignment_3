# Name: Paul Schmidt
# OSU Email: schmipau@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Part 2
# Due Date: 2/9/2026
# Description: Stack class using the dynamic array
# methods from previous assignment to maintain stack.
# Methods implemented to push, pop, and top the stack.


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Pushes value to top of stack.

        :param value:   value to push

        :return:        None
        """
        # Use the dynamic array method to append values
        self._da.append(value)



    def pop(self) -> object:
        """
        Removes top value from stack and returns value.

        :param :        None

        :return:        value
        """
        # Raise exception if stack is empty
        if self.is_empty():
            raise StackException

        # Get the last index based on length
        last_index = self._da.length() - 1
        return_val = self._da.get_at_index(last_index)

        # Remove the value at the index and return the value
        self._da.remove_at_index(last_index)
        return return_val


    def top(self) -> object:
        """
        Returns the top value of the stack without changing stack.

        :param :        None

        :return:        value
        """
        # Raise exception if stack is empty
        if self.is_empty():
            raise StackException

        # Get the last index based on length and return value
        last_index = self._da.length() - 1
        return_val = self._da.get_at_index(last_index)
        return return_val


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
