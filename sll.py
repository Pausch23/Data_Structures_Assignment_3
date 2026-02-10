# Name: Paul Schmidt
# OSU Email: schmipau@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Part 1
# Due Date: 2/9/2026
# Description: Singly linked list class with methods to maintain
# the list. Class contains methods to insert, remove,
# and slice elements in the linked list. There is a method
# to count and find certain elements.



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
        Inserts value at the front of the list.

        :param value:   value to insert at front

        :return:        None
        """
        # Create new node and set to next of sentinel
        if self.is_empty():
            self._head.next = SLNode(value, None)
        else:
            # Preserve next node val
            next_val = self._head.next

            # Create new node and set to next of head
            self._head.next = SLNode(value, None)

            # Set the new nodes next to the preserved next val
            self._head.next.next = next_val


    def insert_back(self, value: object) -> None:
        """
        Inserts value at end of the list.

        :param value:   value to insert at end

        :return:        None
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
        Inserts value at specific index.

        :param index:   index to insert value
        :param value:   value to insert at index

        :return:        None
        """
        # Raise error if index out of bounds
        if index < 0 or index > self.length():
            raise SLLException

        # If insert at front or back, set new node using methods
        if index == 0:
            self.insert_front(value)

        # Start at index 1 after inserting first value
        curr_index = 1
        curr_node = self._head.next

        # Loop through each node and insert at index
        while curr_node:
            if curr_index == index:

                # Preserve curr node and set new node to next
                next_node = curr_node.next
                curr_node.next = SLNode(value, None)
                curr_node.next.next = next_node

            # Increment index counter and set current to next node and loop
            curr_index += 1
            curr_node = curr_node.next


    def remove_at_index(self, index: int) -> None:
        """
        Removes node at specific index in list.

        :param index:   index to remove node

        :return:        None
        """
        # Raise error if index out of bounds
        if index < 0 or index >= self.length():
            raise SLLException

        # Set index counter, head, and next pointer
        curr_index = 0
        head_node = self._head
        curr_node = head_node.next

        # Loop through list and find value to remove
        while curr_node:
            if curr_index == index:

                # Set prev to head, next to head's next
                prev_node = head_node
                next_node = curr_node.next

                # Previous becomes next, removing the current node
                prev_node.next = next_node

                # Return once index removed
                return

            # Add to counter, set head to current, current to next
            curr_index += 1
            head_node = curr_node
            curr_node = curr_node.next


    def remove(self, value: object) -> bool:
        """
        Removes node where input value matches node value that occurs first.

        :param value:   value to remove

        :return:        bool based on if value was removed
        """
        # Set index counter, head, and next pointer
        curr_index = 0
        head_node = self._head
        curr_node = head_node.next

        # Loop through list and find value to remove
        while curr_node:
            if curr_node.value == value:

                # Set prev to head, next to head's next
                prev_node = head_node
                next_node = curr_node.next

                # Previous becomes next, removing the current node
                prev_node.next = next_node

                # Return True once index removed
                return True

            # Add to counter, set head to current, current to next
            curr_index += 1
            head_node = curr_node
            curr_node = curr_node.next

        # Return false if no value found
        return False


    def count(self, value: object) -> int:
        """
        Counts the total number of values parameter in list.

        :param value:   value to count

        :return:        count of value in list
        """
        # Set value counter and next node to start of list
        val_count = 0
        next_node = self._head.next

        while next_node:
            # Add to counter if the node value is match
            if next_node.value == value:
                val_count += 1
            next_node = next_node.next

        # Return the total count of value in list
        return val_count


    def find(self, value: object) -> bool:
        """
        Returns a bool based on if the value parameter is currently in the linked list

        :param value: value to find in linked list

        :return:      returns True or False based on value in list
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
        Returns a sliced linked list from the main linked list.

        :param start_index: beginning index in main list
        :param size:        size of return list

        :return:            returns new sliced linked list
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

        # Raise exception if the end index is outside the list
        if end_index >= self.length():
            raise SLLException

        # Create return list and return empty list if size is 0
        new_list = LinkedList()
        if size == 0:
            return new_list

        # Set index counter and begin loop at head
        curr_index = 0
        curr_node = self._head

        # Continue looping until new list is at full length
        while new_list.length() < calculated_length:
            curr_node = curr_node.next

            # If the current node is to be sliced, add to return list
            if start_index == curr_index:
                new_list.insert_back(curr_node.value)
                start_index += 1
            curr_index += 1

        # Return new list
        return new_list




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
