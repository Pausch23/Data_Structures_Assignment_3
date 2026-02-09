# Name: Paul Schmidt
# OSU Email: schmipau@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/9/2026
# Description: Single linked list


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        # """
        # Create new node and set to next of sentinel
        if self.is_empty():
            self._head.next = SLNode(value, None)
        else:
            # Preserve next node val
            next_val = self._head.next

            # Create new node and set to next of head
            self._head.next = SLNode(value, None)

            # set the new nodes next to the preserved next val
            self._head.next.next = next_val


    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        # If list is empty, set first val in list
        if self.is_empty():
            self._head.next = SLNode(value, None)
        else:
            next_node = self._head.next

            # While the next node is not None, loop until None or at end
            while next_node.next:
                next_node = next_node.next

            # Set the last node to new node value
            next_node.next = SLNode(value, None)


    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        # Raise error if index out of bounds
        if index < 0 or index > self.length():
            raise SLLException

        # If insert at front or back, set new node using methods
        if index == 0:
            self.insert_front(value)

        # Insert val logic if not front, back, or invalid
        curr_index = 1
        curr_node = self._head.next

        while curr_node:
            if curr_index == index:
                # Preserve curr node
                next_node = curr_node.next
                curr_node.next = SLNode(value, None)
                curr_node.next.next = next_node
            curr_index += 1
            curr_node = curr_node.next



    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        # Raise error if index out of bounds
        if index < 0 or index >= self.length():
            raise SLLException

        # Insert val logic if not front, back, or invalid
        curr_index = 0
        head_node = self._head
        curr_node = head_node.next

        while curr_node:
            if curr_index == index:
                prev_node = head_node
                next_node = curr_node.next
                prev_node.next = next_node
                return

            curr_index += 1
            head_node = curr_node
            curr_node = curr_node.next



    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        # Insert val logic if not front, back, or invalid
        curr_index = 0
        head_node = self._head
        curr_node = head_node.next

        while curr_node:
            if curr_node.value == value:
                prev_node = head_node
                next_node = curr_node.next
                prev_node.next = next_node
                return True

            curr_index += 1
            head_node = curr_node
            curr_node = curr_node.next

        # Return false if no value found
        return False




    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        val_count = 0
        next_node = self._head.next
        while next_node:
            if next_node.value == value:
                val_count += 1
            next_node = next_node.next
        return val_count


    def find(self, value: object) -> bool:
        """
        Returns a bool based on if the value parameter is currently in the linked list

        :param value: value to find in linked list

        :return: returns True or False based on value in list
        """
        # Set next node to next of head
        next_node = self._head.next

        # Loop until next node is None, indicating end of list
        while next_node:

            # if the next node's value is value to find, return True
            if next_node.value == value:
                return True
            next_node = next_node.next

        # Return False is value not found
        return False


    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        # Check that start index is valid
        if start_index < 0 or start_index >= self.length():
            raise SLLException

        # Check that size is valid
        if size < 0 or size > self.length():
            raise SLLException

        # Calculate end index and array length
        end_index = start_index + (size - 1)
        calculated_length = abs(start_index - end_index) + 1

        new_list = LinkedList()

        curr_index = 0
        curr_node = self._head
        while curr_index < calculated_length:
            curr_node = curr_node.next
            if start_index == curr_index:
                print(curr_node)
            curr_index += 1




# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    #
    # print("\n# insert_front example 1")
    # test_cases = ["A", "B", "C"]
    # lst = LinkedList()
    # for case in test_cases:
    #     lst.insert_front(case)
    #
    # print(lst.length())


    #
    # print("\n# insert_back example 1")
    # test_cases = ["C", "B", "A"]
    # lst = LinkedList()
    # for case in test_cases:
    #     lst.insert_back(case)
    #     print(lst)


    #
    # print("\n# insert_at_index example 1")
    # lst = LinkedList()
    # test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    # for index, value in test_cases:
    #     print("Inserted", value, "at index", index, ": ", end="")
    #     print("Length:", lst.length(),lst)
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #



    # print("\n# remove_at_index example 1")
    # lst = LinkedList([1, 2, 3, 4, 5, 6])
    # print(f"Initial LinkedList : {lst}")
    # for index in [0, 2, 0, 2, 2, -2]:
    #     print("Removed at index", index, ": ", end="")
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))



    # print("\n# remove example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [7, 3, 3, 3, 3]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# remove example 2")
    # lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    # for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
    #     print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
    #           f"\n {lst}")
    #
    # print("\n# count example 1")
    # lst = LinkedList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))



    # print("\n# find example 1")
    # lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    # print(lst)
    # print(lst.find("Waldo"))
    # print(lst.find("Superman"))
    # print(lst.find("Santa Claus"))



    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")
