#!/usr/bin/python3

 def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The position in the list to replace.
        element (int): The new value to insert at the position.

    Returns:
        A new list with the element replaced, or a copy of the original list if the index is invalid.
    """
    # Create a copy of the original list
    new_list = my_list[:]

    # Check if index is within the valid range
    if idx < 0 or idx >= len(my_list):
        return new_list

    # Replace the element at the specified index
    new_list[idx] = element
    return new_list
